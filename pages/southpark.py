
import base64
import html
import textwrap
from pathlib import Path

import pandas as pd
import streamlit as st

from utils.styling.components.headers import (
    render_page_header,
    render_section_header,
)
from utils.styling.components.html import render_html
from utils.styling.headers import apply_header_styles
from utils.styling.southpark import apply_southpark_styles
from utils.styling.backgroundhelper import render_background


# =============================================================================
# PAGE STYLING
# =============================================================================

apply_header_styles()
apply_southpark_styles()

render_background(
    image_name="southparkbackground.jpg",
    overlay=0.2,
)


# =============================================================================
# GOOGLE SHEET
# =============================================================================

SHEET_ID = "1_6G8-E-YvJ2vN1c2ZWT0A5bkA7miUs_Jm_FsNmTvR3g"
GID = "0"

SHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export"
    f"?format=csv&gid={GID}"
)


@st.cache_data(ttl=10)
def load_episodes():
    """Load episode rankings from Google Sheets."""
    return pd.read_csv(SHEET_URL)


# =============================================================================
# HELPERS
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def safe_text(value, fallback="—"):
    """Escape text so it displays safely inside HTML."""

    if value is None:
        return html.escape(fallback)

    if pd.isna(value) or str(value).strip() == "":
        return html.escape(fallback)

    return html.escape(str(value))


def render_html(content):
    """Render HTML without Markdown interpreting indentation as code."""

    cleaned_html = textwrap.dedent(content).strip()

    # Remove leading indentation from every line.
    cleaned_html = "\n".join(
        line.lstrip()
        for line in cleaned_html.splitlines()
    )

    st.markdown(
        cleaned_html,
        unsafe_allow_html=True,
    )


def get_character_image(character):
    """Find a character image and convert it to a base64 data URI."""

    filename = (
        str(character)
        .lower()
        .strip()
        .replace(" ", "_")
        .replace(".", "")
    )

    image_path = (
        PROJECT_ROOT
        / "images"
        / "characters"
        / f"{filename}.png"
    )

    if not image_path.is_file():
        return None

    encoded = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    return f"data:image/png;base64,{encoded}"


def get_rating_color(rating):
    """Create a dark-red to yellow to bright-green rating gradient."""

    if pd.isna(rating):
        return "#777777"

    rating = max(1, min(10, float(rating)))

    if rating <= 5.5:
        progress = (rating - 1) / 4.5
        start = (125, 0, 0)
        end = (245, 190, 0)
    else:
        progress = (rating - 5.5) / 4.5
        start = (245, 190, 0)
        end = (0, 200, 83)

    rgb = [
        int(start[i] + (end[i] - start[i]) * progress)
        for i in range(3)
    ]

    return f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})"


def rating_badge(rating, detail=False):
    """Generate a rating badge for the episode list or detail page."""

    if pd.isna(rating):
        return '<div class="rating-badge rating-unrated">—</div>'

    color = get_rating_color(rating)
    detail_class = " detail-rating-badge" if detail else ""

    return (
        f'<div class="rating-badge{detail_class}" '
        f'style="background-color: {color};">'
        f'{float(rating):g}'
        f'</div>'
    )


def render_stat_card(label, value, subtitle=""):
    """Render a reusable statistics card."""

    subtitle_html = (
        f'<div class="stat-small">{safe_text(subtitle)}</div>'
        if subtitle
        else ""
    )

    render_html(
        f"""
        <div class="stat-card">
            <div class="stat-label">{safe_text(label)}</div>
            <div class="stat-number">{safe_text(value)}</div>
            {subtitle_html}
        </div>
        """
    )


# =============================================================================
# LOAD AND CLEAN DATA
# =============================================================================

episodes = load_episodes()

episodes.columns = episodes.columns.str.strip()

for column in ["Season", "Episode", "Rating"]:
    episodes[column] = pd.to_numeric(
        episodes[column],
        errors="coerce",
    )

episodes = (
    episodes
    .dropna(subset=["Season", "Episode", "Title"])
    .reset_index(drop=True)
)


# =============================================================================
# SESSION STATE
# =============================================================================

if "selection" not in st.session_state:
    st.session_state.selection = None

# Reset selection if the spreadsheet changes.
if (
    st.session_state.selection is not None
    and not 0 <= st.session_state.selection < len(episodes)
):
    st.session_state.selection = None


# =============================================================================
# EPISODE DETAIL PAGE
# =============================================================================

if st.session_state.selection is not None:

    episode = episodes.iloc[st.session_state.selection]

    # Back button
    if st.button("← Back to episodes"):
        st.session_state.selection = None
        st.rerun()

    # Episode information
    season = int(episode["Season"])
    number = int(episode["Episode"])
    title = safe_text(episode["Title"])

    favorite = safe_text(
        episode.get("Favorite Character")
    )

    rewatch = safe_text(
        episode.get("Would I Rewatch?")
    )

    comments = safe_text(
        episode.get("Comments"),
        fallback="Nothing to give yet!",
    )

    # Episode detail card
    render_html(
        f"""
        <div class="episode-detail-card">

            <div class="episode-label">
                SEASON {season} • EPISODE {number}
            </div>

            <div class="episode-detail-title">
                {title}
            </div>

            <div class="detail-rating-wrapper">
                {rating_badge(episode["Rating"], detail=True)}
            </div>

            <div class="episode-info">
                <strong>Favorite Character:</strong> {favorite}
            </div>

            <div class="episode-info">
                <strong>Would I Rewatch?</strong> {rewatch}
            </div>

            <div class="episode-comments-title">
                MY THOUGHTS
            </div>

            <div class="episode-comments">{comments}</div>

        </div>
        """
    )


# =============================================================================
# EPISODE BROWSER
# =============================================================================

else:

    # -------------------------------------------------------------------------
    # Page Header
    # -------------------------------------------------------------------------

    render_page_header(
        title="South Park Episode Rankings",
        subtitle=(
            "Rating all of the episodes for my super sexy girlfriend, "
            "so that she also knows that I am paying attention and love her."
        ),
        theme="southpark",
    )

    # -------------------------------------------------------------------------
    # Season Selector
    # -------------------------------------------------------------------------

    seasons = sorted(
        episodes["Season"]
        .dropna()
        .astype(int)
        .unique()
    )

    if not seasons:
        st.info("No episodes found in the spreadsheet.")
        st.stop()

    selected_season = st.selectbox(
        "Choose a season",
        seasons,
        format_func=lambda season: f"Season {season}",
    )

    render_html(
        f'<div class="season-heading">SEASON {selected_season}</div>'
    )

    # -------------------------------------------------------------------------
    # Filter Episodes
    # -------------------------------------------------------------------------

    season_episodes = episodes[
        episodes["Season"] == selected_season
    ]

    # -------------------------------------------------------------------------
    # Episode List
    # -------------------------------------------------------------------------

    for index, episode in season_episodes.iterrows():

        episode_number = int(episode["Episode"])
        title = str(episode["Title"])
        rating = episode["Rating"]

        episode_col, rating_col = st.columns(
            [5, 1],
            vertical_alignment="center",
        )

        # Episode Button
        with episode_col:

            clicked = st.button(
                f"E{episode_number:02d}  •  {title}",
                key=f"episode_{index}",
                use_container_width=True,
            )

        # Rating Badge
        with rating_col:

            render_html(
                f"""
                <div class="rating-wrapper">
                    {rating_badge(rating)}
                </div>
                """
            )

        # Open Episode
        if clicked:
            st.session_state.selection = index
            st.rerun()

    # =========================================================================
    # STATS
    # =========================================================================

    render_section_header(
        title="STATS",
        theme="southpark",
    )

    # -------------------------------------------------------------------------
    # Episodes Watched
    # -------------------------------------------------------------------------

    watched = (
        episodes["Watched?"]
        .astype(str)
        .str.strip()
        .str.upper()
        .isin(["TRUE", "YES", "1"])
    )

    watched_count = int(watched.sum())
    total_episodes = len(episodes)

    watched_percent = (
        watched_count / total_episodes * 100
        if total_episodes
        else 0
    )

    # -------------------------------------------------------------------------
    # Average Rating
    # -------------------------------------------------------------------------

    rated_episodes = episodes["Rating"].dropna()

    average_display = (
        f"{rated_episodes.mean():.1f}/10"
        if not rated_episodes.empty
        else "—"
    )

    # -------------------------------------------------------------------------
    # Stat Cards
    # -------------------------------------------------------------------------

    stat1, stat2 = st.columns(2)

    with stat1:
        render_stat_card(
            label="EPISODES WATCHED",
            value=f"{watched_count} / {total_episodes}",
            subtitle=f"{watched_percent:.1f}% complete",
        )

    with stat2:
        render_stat_card(
            label="AVERAGE RATING",
            value=average_display,
        )

    # =========================================================================
    # FAVORITE CHARACTERS
    # =========================================================================

    favorite_characters = (
        episodes["Favorite Character"]
        .dropna()
        .astype(str)
        .str.strip()
    )

    favorite_characters = favorite_characters[
        favorite_characters != ""
    ]

    character_counts = (
        favorite_characters
        .value_counts()
        .head(10)
    )

    render_html(
        '<div class="character-heading">FAVORITE CHARACTERS</div>'
    )

    # -------------------------------------------------------------------------
    # No Character Data
    # -------------------------------------------------------------------------

    if character_counts.empty:

        render_html(
            """
            <div class="no-stats">
                No favorite characters entered yet!
            </div>
            """
        )

    # -------------------------------------------------------------------------
    # Character Rankings
    # -------------------------------------------------------------------------

    else:

        max_count = character_counts.max()

        for character, count in character_counts.items():

            character_image = get_character_image(character)

            width = (
                count / max_count * 100
                if max_count
                else 0
            )

            # Character Picture
            if character_image:
                picture_html = (
                    f'<img src="{character_image}" '
                    f'class="character-image" alt="">'
                )
            else:
                picture_html = (
                    '<div class="character-placeholder">?</div>'
                )

            # Character Card
            character_html = f"""
<div class="character-row">

    <div class="character-picture">
        {picture_html}
    </div>

    <div class="character-content">

        <div class="character-name">
            {safe_text(character)}
        </div>

        <div class="character-bar-area">

            <div
                class="character-bar"
                style="width: {width}%;"
            ></div>

            <div class="character-count">
                {count}
            </div>

        </div>

    </div>

</div>
"""

            render_html(character_html)
