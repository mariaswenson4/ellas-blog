
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

# =============================================================================
# PAGE STYLING
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

render_page_header(
    eyebrow="THE GAME OF YELLOW CARS",
    title="BINGO Tracker",
    subtitle="Keeping a tally and tracking stats of all the BINGOS we see.",
    theme="bingo",
)

# =============================================================================
# BINGO RULES CARD
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
# GOOGLE SHEETS CONNECTION
# =============================================================================

@st.cache_resource
def get_google_client():

    credentials = Credentials.from_service_account_info(
        dict(st.secrets["gcp_service_account"]),
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets"
        ]
    )

    return gspread.authorize(credentials)


# =============================================================================
# GOOGLE SHEETS CONNECTION
# =============================================================================

def get_worksheet():

    client = get_google_client()

    try:
        spreadsheet = client.open_by_key(SHEET_ID)

        worksheet = spreadsheet.get_worksheet_by_id(GID)

        return worksheet

    except PermissionError as e:

        st.error("Google Sheets permission error.")

        # Reveal the underlying API error
        original_error = e.__cause__

        if original_error is not None:
            st.write("Google API response:")
            st.code(str(original_error))

        raise

    except Exception as e:

        st.error("Google Sheets connection failed.")
        st.exception(e)

        raise
# =============================================================================
# LOAD BINGO DATA
# =============================================================================

@st.cache_data(ttl=60)
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

        st.error(
            "Unable to load BINGO History."
        )

        st.exception(e)
