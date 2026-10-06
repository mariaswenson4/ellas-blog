import pandas as pd
import streamlit as st
import base64
from pathlib import Path 

from utils.styling.southpark import apply_southpark_styles


# =============================================================================
# PAGE STYLING
# =============================================================================

apply_southpark_styles()


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
    return pd.read_csv(SHEET_URL)


# =============================================================================
# RATING COLOR
# =============================================================================

def get_character_image(character):
    """Return a character image as a base64 data URI."""

    filename = (
        str(character)
        .lower()
        .strip()
        .replace(" ", "_")
        .replace(".", "")
    )

    project_root = Path(__file__).resolve().parent.parent

    path = (
        project_root
        / "images"
        / "characters"
        / f"{filename}.png"
    )

    if not path.exists():
        return None

    encoded = base64.b64encode(
        path.read_bytes()
    ).decode("utf-8")

    return f"data:image/png;base64,{encoded}"

def get_rating_color(rating):
    """Create a smooth dark-red to bright-green rating gradient."""

    if pd.isna(rating):
        return "#777777"

    rating = max(1, min(10, float(rating)))

    # Dark red -> yellow
    if rating <= 5.5:
        progress = (rating - 1) / 4.5

        start = (125, 0, 0)
        end = (245, 190, 0)

    # Yellow -> bright green
    else:
        progress = (rating - 5.5) / 4.5

        start = (245, 190, 0)
        end = (0, 200, 83)

    red = int(
        start[0] + (end[0] - start[0]) * progress
    )

    green = int(
        start[1] + (end[1] - start[1]) * progress
    )

    blue = int(
        start[2] + (end[2] - start[2]) * progress
    )

    return f"rgb({red}, {green}, {blue})"


# =============================================================================
# LOAD + CLEAN DATA
# =============================================================================

episodes = load_episodes()
episodes.columns = episodes.columns.str.strip()
episodes["Season"] = pd.to_numeric(
    episodes["Season"],
    errors="coerce",
)

episodes["Episode"] = pd.to_numeric(
    episodes["Episode"],
    errors="coerce",
)

episodes["Rating"] = pd.to_numeric(
    episodes["Rating"],
    errors="coerce",
)

episodes = episodes.dropna(
    subset=["Season", "Episode", "Title"]
)

episodes = episodes.reset_index(drop=True)


# =============================================================================
# SESSION STATE
# =============================================================================

if "selection" not in st.session_state:
    st.session_state.selection = None


# =============================================================================
# EPISODE DETAIL PAGE
# =============================================================================

if st.session_state.selection is not None:

    episode = episodes.iloc[
        st.session_state.selection
    ]

    # -------------------------------------------------------------------------
    # Back Button
    # -------------------------------------------------------------------------

    if st.button("← Back to episodes"):
        st.session_state.selection = None
        st.rerun()

    # -------------------------------------------------------------------------
    # Values
    # -------------------------------------------------------------------------

    rating = episode["Rating"]

    favorite_character = episode.get(
        "Favorite Character",
        "",
    )

    comments = episode.get(
        "Comments",
        "",
    )

    rewatch = episode.get(
        "Would I Rewatch?",
        "",
    )

    if pd.isna(favorite_character):
        favorite_character = "—"

    if pd.isna(comments):
        comments = "Nothing to give yet!"

    if pd.isna(rewatch):
        rewatch = "—"

    # -------------------------------------------------------------------------
    # Rating
    # -------------------------------------------------------------------------

    if pd.isna(rating):

        detail_rating = """
<div class="rating-badge rating-unrated">
    —
</div>
"""

    else:

        rating_color = get_rating_color(rating)

        detail_rating = f"""
<div
    class="rating-badge detail-rating-badge"
    style="background-color: {rating_color};"
>
    {rating:g}
</div>
"""

    # -------------------------------------------------------------------------
    # Episode Card
    # -------------------------------------------------------------------------

    st.markdown(
        f"""
<div class="episode-detail-card">

<div class="episode-label">
    SEASON {int(episode["Season"])} • EPISODE {int(episode["Episode"])}
</div>

<div class="episode-detail-title">
    {episode["Title"]}
</div>

<div class="detail-rating-wrapper">
    {detail_rating}
</div>

<div class="episode-info">
    <strong>Favorite Character:</strong>
    {favorite_character}
</div>

<div class="episode-info">
    <strong>Would I Rewatch?</strong>
    {rewatch}
</div>

<div class="episode-comments-title">
    MY THOUGHTS
</div>

<div class="episode-comments">
    {comments}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# =============================================================================
# SEASON / EPISODE BROWSER
# =============================================================================

else:

    # -------------------------------------------------------------------------
    # Header
    # -------------------------------------------------------------------------

    st.markdown(
        """
<div class="southpark-title">
    South Park Episode Rankings
</div>

<div class="southpark-subtitle">
    Rating all of the episodes for my super sexy girlfriend,
    so that she also knows that I am paying attention and love her.
</div>
""",
        unsafe_allow_html=True,
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

    selected_season = st.selectbox(
        "Choose a season",
        seasons,
        format_func=lambda season: f"Season {season}",
    )

    # -------------------------------------------------------------------------
    # Filter Episodes
    # -------------------------------------------------------------------------

    season_episodes = episodes[
        episodes["Season"] == selected_season
    ]

    # -------------------------------------------------------------------------
    # Season Heading
    # -------------------------------------------------------------------------

    st.markdown(
        f"""
<div class="season-heading">
    SEASON {selected_season}
</div>
""",
        unsafe_allow_html=True,
    )

    # -------------------------------------------------------------------------
    # Episode List
    # -------------------------------------------------------------------------

    for index, episode in season_episodes.iterrows():

        episode_number = int(
            episode["Episode"]
        )

        title = str(
            episode["Title"]
        ).replace('"', "")

        rating = episode["Rating"]

        # ---------------------------------------------------------------------
        # Columns
        # ---------------------------------------------------------------------

        episode_col, rating_col = st.columns(
            [5, 1],
            vertical_alignment="center",
        )

        # ---------------------------------------------------------------------
        # Episode Button
        # ---------------------------------------------------------------------

        with episode_col:

            clicked = st.button(
                f"E{episode_number:02d}  •  {title}",
                key=f"episode_{index}",
                use_container_width=True,
            )

        # ---------------------------------------------------------------------
        # Rating Badge
        # ---------------------------------------------------------------------

        with rating_col:

            if pd.isna(rating):

                st.markdown(
                    """
<div class="rating-wrapper">
    <div class="rating-badge rating-unrated">
        —
    </div>
</div>
""",
                    unsafe_allow_html=True,
                )

            else:

                rating_color = get_rating_color(
                    rating
                )

                st.markdown(
                    f"""
<div class="rating-wrapper">
    <div
        class="rating-badge"
        style="background-color: {rating_color};"
    >
        {rating:g}
    </div>
</div>
""",
                    unsafe_allow_html=True,
                )

        # ---------------------------------------------------------------------
        # Open Episode
        # ---------------------------------------------------------------------

        if clicked:
            st.session_state.selection = index
            st.rerun()

            # =========================================================================
    # STATS
    # =========================================================================

    st.markdown(
        """
<div class="stats-heading">
    STATS
</div>
""",
        unsafe_allow_html=True,
    )


    # -------------------------------------------------------------------------
    # Watched Episodes
    # -------------------------------------------------------------------------

    watched = (
        episodes["Watched?"]
        .astype(str)
        .str.strip()
        .str.upper()
        .isin(["TRUE", "YES", "1"])
    )

    watched_count = watched.sum()
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

    if len(rated_episodes) > 0:
        average_rating = rated_episodes.mean()
        average_display = f"{average_rating:.1f}/10"
    else:
        average_display = "—"


    # -------------------------------------------------------------------------
    # Stat Cards
    # -------------------------------------------------------------------------

    stat1, stat2 = st.columns(2)

    with stat1:
        st.markdown(
            f"""
<div class="stat-card">
    <div class="stat-label">EPISODES WATCHED</div>
    <div class="stat-number">
        {watched_count} / {total_episodes}
    </div>
    <div class="stat-small">
        {watched_percent:.1f}% complete
    </div>
</div>
""",
            unsafe_allow_html=True,
        )

    with stat2:
        st.markdown(
            f"""
<div class="stat-card">
    <div class="stat-label">AVERAGE RATING</div>
    <div class="stat-number">
        {average_display}
    </div>
</div>
""",
            unsafe_allow_html=True,
        )

    # -------------------------------------------------------------------------
    # Favorite Character Counts
    # -------------------------------------------------------------------------

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


    st.markdown(
        """
<div class="character-heading">
    FAVORITE CHARACTERS
</div>
""",
        unsafe_allow_html=True,
    )


    if character_counts.empty:

        st.markdown(
            """
<div class="no-stats">
    No favorite characters entered yet!
</div>
""",
            unsafe_allow_html=True,
        )

    else:

        max_count = character_counts.max()

        for character, count in character_counts.items():

            image = get_character_image(character)

            width = (
                count / max_count * 100
                if max_count
                else 0
            )

            if image:
                picture_html = (
                    f'<img src="{image}" '
                    f'class="character-image">'
                )
            else:
                picture_html = (
                    '<div class="character-placeholder">?</div>'
                )

            character_html = f"""
<div class="character-row">
<div class="character-picture">{picture_html}</div>
<div class="character-content">
<div class="character-name">{character}</div>
<div class="character-bar-area">
<div class="character-bar" style="width: {width}%;"></div>
<div class="character-count">{count}</div>
</div>
</div>
</div>
"""

            st.markdown(
                character_html,
                unsafe_allow_html=True,
            )