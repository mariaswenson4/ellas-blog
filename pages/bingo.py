
import streamlit as st
import pandas as pd
import gspread
from datetime import date
from google.oauth2.service_account import Credentials
from utils.styling.bingo import apply_bingo_styles
from utils.styling.components.html import render_html
from utils.styling.headers import apply_header_styles
from utils.styling.backgroundhelper import render_background
from utils.styling.components.headers import (
    render_page_header,
    render_section_header,
)
import plotly.graph_objects as go

# =============================================================================
# Configure Page & Render Background
# =============================================================================
apply_header_styles()
apply_bingo_styles()
render_background(
    image_name="bingobackground.jpg",
    overlay=0.35,
    size="cover",
    position="center",
    attachment="fixed",
)
render_page_header(
    eyebrow="THE GAME OF YELLOW CARS",
    title="BINGO Tracker",
    subtitle="Keeping a tally and tracking stats of all the BINGOS we see.",
    theme="bingo",
)
# =============================================================================
# GOOGLE SHEET CONFIGURATION
# =============================================================================
SHEET_ID = "1267M3xNsCRh_0MbEzs4tXhrZGGdcC7TkfDa2CSdtA7I"
GID = 0
COLUMNS = [
    "Date of Travel",
    "BINGO Count",
    "Who Saw?",
    "Traveling To?"
]
# =============================================================================
# Read in the Bingo Rules HTML snippet and render it
# =============================================================================
render_html("""
<div class="bingo-rules-card">

    <div class="bingo-rules-eyebrow">
        THE OFFICIAL RULEBOOK
    </div>

    <div class="bingo-rules-title">
        BINGO Rules
    </div>

    <div class="bingo-rule">
        <span class="bingo-rule-number">01</span>
        <div>
            <strong>When to call "BINGO!"</strong>
            <p>
                A BINGO may be called whenever a yellow car is spotted on the road.
                It can only be called out ONCE per car ride, but if the car turns off at any point, a new BINGO may be called upon ignition.
            </p>
        </div>
    </div>

    <div class="bingo-rule">
        <span class="bingo-rule-number">02</span>
        <div>
            <strong>What constitutes a BINGO?</strong>
            <p>
                A BINGO is defined as a yellow car that is spotted on the road.
                It must not be attached to a branded vehicle, such as a taxi, delivery truck, or school bus, and must be a standard vehicle.
            </p>
        </div>
    </div>

    <div class="bingo-rule">
        <span class="bingo-rule-number">03</span>
        <div>
            <strong>One car = One BINGO</strong>
            <p>
                Each yellow car spotted counts as one BINGO, regardless of the type of car. Even a slug bug. 
            </p>
        </div>
    </div>

    <div class="BINGO-rules-footer">
        Exception: Ella must always win according to her bendable rules.
    </div>

</div>
""")

# =============================================================================
# Read in Google Sheet credentials & authorize them. This is from T&J Analytics
# =============================================================================
@st.cache_resource
def authorize_client():
    credentials = Credentials.from_service_account_info(
        dict(st.secrets["gcp_service_account"]),
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return gspread.authorize(credentials)
# =============================================================================
# Render Google Sheet
# =============================================================================
def get_worksheet():
    client = authorize_client()
    try:
        spreadsheet = client.open_by_key(SHEET_ID)
        worksheet = spreadsheet.get_worksheet_by_id(GID)
        return worksheet
    except PermissionError as e: 
    # Provides feedback if there is an error reading it in API wise
        st.error("Google Sheets permission error.")
        original_error = e.__cause__
        if original_error is not None:
            st.write("Google API response:")
            st.code(str(original_error))
        raise
    except Exception as e:
    # Catches any other exceptions that may occur during the connection process and provides feedback to the user.
        st.error("Google Sheets connection failed.")
        st.exception(e)
        raise
# =============================================================================
# Load in the Bingo Data from Google Sheet
# =============================================================================
@st.cache_data(ttl=60) # Refreshes every 60 seconds. Lower if not good.
def load_bingo_data():

    worksheet = get_worksheet()

    records = worksheet.get_all_records()

    # Load actual Google Sheet column names
    df = pd.DataFrame(records)

    # Remove accidental spaces from headers
    df.columns = df.columns.str.strip()

    # Check that all expected columns exist
    missing_columns = [
        col for col in COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}. "
            f"Actual Google Sheet columns: {df.columns.tolist()}"
        )

    df = df[COLUMNS].copy()

    if df.empty:
        return df

    # Convert dates
    df["Date of Travel"] = pd.to_datetime(
        df["Date of Travel"],
        errors="coerce"
    )

    # Convert counts
    df["BINGO Count"] = pd.to_numeric(
        df["BINGO Count"],
        errors="coerce"
    )

    return df


# =============================================================================
# SAVE NEW SIGHTING
# =============================================================================

def save_bingo_sighting(
    travel_date,
    bingo_count,
    who_saw,
    traveling_to
):

    worksheet = get_worksheet()

    worksheet.append_row(
        [
            travel_date.strftime("%Y-%m-%d"),
            int(bingo_count),
            who_saw,
            traveling_to
        ],
        value_input_option="USER_ENTERED"
    )

    # Refresh data after saving
    load_bingo_data.clear()
# =============================================================================
# ADD BINGO SIGHTING CARD
# =============================================================================

with st.container(border=True, key="bingo_form_card"):

    st.markdown("### Add a BINGO Sighting Here!")
    st.caption("Spotted a BINGO? Add it to our collection and see our history and stats below!")

    with st.form(
        key="bingo_sighting_form",
        clear_on_submit=True,
        border=False
    ):

        col1, col2 = st.columns(2, gap="medium")

        with col1:
            travel_date = st.date_input(
                "Date of Travel",
                value=date.today(),
                max_value=date.today()
            )

        with col2:
            bingo_count = st.number_input(
                "BINGO Count",
                min_value=0,
                value=1,
                step=1
            )

        who_saw = st.selectbox(
            "Who Saw?",
            options=["Maria", "Ella"]
        )
        traveling_to = st.text_input(
            "Traveling To?",
            placeholder="Enter destination..."
        )

        submitted = st.form_submit_button(
            "Save Trip",
            use_container_width=True,
            type="primary"
        )
# =============================================================================
# HANDLE FORM SUBMISSION
# =============================================================================

if submitted:

    try:

        save_bingo_sighting(
            travel_date=travel_date,
            bingo_count=bingo_count,
            who_saw=who_saw,
            traveling_to=traveling_to
        )

        st.success(
            "BINGO count saved !"
        )

    except Exception as e:

        st.error(
            "Unable to record this BINGO sighting! Try again later pookie."
        )

        st.exception(e)


# 
# BINGO HISTORY
# =============================================================================

st.write("")

with st.container(border=True, key="bingo_history_card"):

    st.markdown("### BINGO History")
    st.caption("Comprehensive record of all of the BINGO's that we have recorded.")

    try:

        df = load_bingo_data()

        if df.empty:

            st.info(
                "No BINGO sightings recorded yet!"
            )

        else:

            # Sort newest sightings first
            df = df.sort_values(
                "Date of Travel",
                ascending=False
            )

            # Display history
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={

                    "Date of Travel":
                        st.column_config.DateColumn(
                            "Date of Travel",
                            format="MM/DD/YYYY"
                        ),

                    "BINGO Count":
                        st.column_config.NumberColumn(
                            "BINGO Count",
                            format="%d"
                        ),

                    "Who Saw?":
                        st.column_config.TextColumn(
                            "Who Saw?"
                        ),
                    "Traveling To?":
                        st.column_config.TextColumn(
                            "Traveling To?"
                        )
                }
            )

    except Exception as e:
        st.error("Unable to load BINGO History.")
        st.exception(e)




# =============================================================================
# BINGO STATISTICS
# =============================================================================

st.write("")

with st.container(border=True, key="bingo_stats_card"):

    st.markdown("### BINGO Statistics")


    try:
        stats_df = load_bingo_data().copy()

        if stats_df.empty:
            st.info("Start recording BINGOs to see your stats!")

        else:

            # =========================================================
            # CLEAN DATA
            # =========================================================

            stats_df["BINGO Count"] = pd.to_numeric(
                stats_df["BINGO Count"],
                errors="coerce"
            ).fillna(0)

            stats_df["Date of Travel"] = pd.to_datetime(
                stats_df["Date of Travel"],
                errors="coerce"
            )

            stats_df["Who Saw?"] = (
                stats_df["Who Saw?"]
                .fillna("")
                .astype(str)
                .str.strip()
                .str.title()
            )

            stats_df["Traveling To?"] = (
                stats_df["Traveling To?"]
                .fillna("")
                .astype(str)
                .str.strip()
            )

            # =========================================================
            # TOTALS
            # =========================================================

            total_bingos = int(stats_df["BINGO Count"].sum())

            maria_bingos = int(
                stats_df.loc[
                    stats_df["Who Saw?"] == "Maria",
                    "BINGO Count"
                ].sum()
            )

            ella_bingos = int(
                stats_df.loc[
                    stats_df["Who Saw?"] == "Ella",
                    "BINGO Count"
                ].sum()
            )

            # =========================================================
            # SCOREBOARD
            # =========================================================

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total BINGOs", total_bingos)

            with col2:
                st.metric("Maria", maria_bingos)

            with col3:
                st.metric("Ella", ella_bingos)

            st.divider()

            # =========================================================
            # BINGOS PER TRIP — MARIA VS ELLA
            # =========================================================

            st.markdown("#### BINGOs Per Trip Graph Comparion Over Trips")
            st.caption(
                "Y-axis represents the number of BINGOs spotted, while the X-axis represents the trip number for each player."
            )

            trip_df = stats_df.dropna(
                subset=["Date of Travel", "BINGO Count"]
            ).copy()

            trip_df = trip_df[
                trip_df["Who Saw?"].isin(["Maria", "Ella"])
            ].copy()

            # Sort trips chronologically
            trip_df = trip_df.sort_values(
                "Date of Travel"
            )

            # Number each person's recorded trips
            trip_df["Trip #"] = (
                trip_df.groupby("Who Saw?").cumcount() + 1
            )

            # Create overlapping line chart
            fig = go.Figure()

            for person, color in [
                ("Maria", "#E45B5B"),
                ("Ella", "#A78BFA")
            ]:

                person_df = trip_df[
                    trip_df["Who Saw?"] == person
                ]

                fig.add_trace(
                    go.Scatter(
                        x=person_df["Trip #"],
                        y=person_df["BINGO Count"],
                        mode="lines+markers",
                        name=person,
                        line=dict(
                            color=color,
                            width=3
                        ),
                        marker=dict(
                            size=9,
                            color=color,
                            line=dict(
                                color="#171B1A",
                                width=2
                            )
                        ),
                        hovertemplate=(
                            "<b>" + person + "</b><br>"
                            "Trip #%{x}<br>"
                            "BINGOs: %{y}<extra></extra>"
                        )
                    )
                )

            # ---------------------------------------------------------
            # CHART STYLING
            # ---------------------------------------------------------

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#E8DED2"),
                height=420,

                margin=dict(
                    l=20,
                    r=20,
                    t=20,
                    b=20
                ),

                xaxis=dict(
                    title="Trip Number",
                    dtick=1,
                    gridcolor="rgba(255,255,255,0.06)",
                    zeroline=False
                ),

                yaxis=dict(
                    title="Bingo Count Per Trip",
                    rangemode="tozero",
                    gridcolor="rgba(255,255,255,0.10)",
                    zeroline=False
                ),

                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="center",
                    x=0.5
                ),

                hovermode="x unified"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.divider()

            
# =========================================================
# MARIA VS ELLA — TOTAL BINGOS
# =========================================================

            st.markdown("#### Maria vs. Ella")
            st.caption("Total yellow cars spotted by each player.")

            fig_totals = go.Figure()

            for person, count, color in [
                ("Maria", maria_bingos, "#E45B5B"),
                ("Ella", ella_bingos, "#A78BFA")
            ]:
                fig_totals.add_trace(
                    go.Bar(
                        y=[person],
                        x=[count],
                        name=person,
                        orientation="h",
                        marker_color=color,
                        text=[count],
                        textposition="outside",
                        hovertemplate=(
                            "<b>" + person + "</b><br>"
                            "Total BINGOs: %{x}<extra></extra>"
                        )
                    )
                )

            fig_totals.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#E8DED2"),
                height=260,
                margin=dict(l=20, r=50, t=20, b=20),
                xaxis=dict(
                    title="Total BINGOs",
                    rangemode="tozero",
                    gridcolor="rgba(255,255,255,0.08)"
                ),
                yaxis=dict(
                    title=None,
                    categoryorder="array",
                    categoryarray=["Ella", "Maria"]
                ),
                showlegend=False,
                bargap=0.4
            )

            st.plotly_chart(
                fig_totals,
                use_container_width=True
            )

            st.divider()


            
            # =========================================================
            # BINGOS BY DESTINATION
            # =========================================================

            st.markdown("#### BINGOs by Destination")
            st.caption("Where do we see the most yellow cars?")

            destination_df = stats_df[
                stats_df["Traveling To?"].ne("")
            ].copy()

            destination_totals = (
                destination_df
                .groupby("Traveling To?")["BINGO Count"]
                .sum()
                .sort_values(ascending=False)
            )

            if not destination_totals.empty:

                # Assign colors to each destination
                destination_colors = {
                    "Stevens Point": "#A78BFA",  # Purple
                    "Madison": "#E45B5B"         # Red
                }

                fig_destinations = go.Figure()

                for destination, count in destination_totals.items():

                    color = destination_colors.get(
                        destination.strip().title(),
                        "#D99532"  # Gold for other destinations
                    )

                    fig_destinations.add_trace(
                        go.Bar(
                            y=[destination],
                            x=[count],
                            name=destination,
                            orientation="h",
                            marker_color=color,
                            text=[int(count)],
                            textposition="outside",
                            hovertemplate=(
                                "<b>" + destination + "</b><br>"
                                "Total BINGOs: %{x}<extra></extra>"
                            )
                        )
                    )

                fig_destinations.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#E8DED2"),
                    height=max(260, len(destination_totals) * 65),
                    margin=dict(l=20, r=55, t=20, b=20),

                    xaxis=dict(
                        title="Total BINGOs",
                        rangemode="tozero",
                        gridcolor="rgba(255,255,255,0.08)"
                    ),

                    yaxis=dict(
                        title="Destination",
                        categoryorder="array",
                        categoryarray=list(
                            reversed(destination_totals.index.tolist())
                        )
                    ),

                    showlegend=False,
                    bargap=0.4
                )

                st.plotly_chart(
                    fig_destinations,
                    use_container_width=True
                )

            else:
                st.info("No destinations recorded yet.")
    except Exception as e:
        st.error("Unable to load BINGO statistics.")
        st.exception(e)
