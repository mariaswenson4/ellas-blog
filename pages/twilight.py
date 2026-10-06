from pathlib import Path

import streamlit as st

from utils.styling.twilight import apply_twilight_styles


# =============================================================================
# PAGE STYLING
# =============================================================================

apply_twilight_styles()

# =============================================================================
# CHAPTERS
# =============================================================================

TWILIGHT_CHAPTERS = {
    1: "First Sight",
    2: "Open Book",
    3: "Phenomenon",
    4: "Invitations",
    5: "Blood Type",
    6: "Scary Stories",
    7: "Nightmare",
    8: "Port Angeles",
    9: "Theory",
    10: "Interrogations",
    11: "Complications",
    12: "Balancing",
    13: "Confessions",
    14: "Mind over Matter",
    15: "The Cullens",
    16: "Carlisle",
    17: "The Game",
    18: "The Hunt",
    19: "Goodbyes",
    20: "Impatience",
    21: "Phone Call",
    22: "Hide-and-Seek",
    23: "The Angel",
    24: "An Impasse",
}
# =============================================================================
# AUDIO LOCATION
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

AUDIO_FOLDER = (
    PROJECT_ROOT
    / "audio"
    / "twilight"
)


# =============================================================================
# HEADER
# =============================================================================

st.markdown(
    """
<div class="twilight-header">
<div class="twilight-eyebrow">Maria's Version of Twilight as an Audiobook</div>
<div class="twilight-title">Twilight</div>
<div class="twilight-subtitle">Read specifically to my hot girlfriend with the utmost enjoyment and pleasure for all first time listeners.</div>
</div>
""",
    unsafe_allow_html=True,
)

# =============================================================================
# FIND AUDIO FILES
# =============================================================================

audio_files = {}

if AUDIO_FOLDER.exists():

    for audio_file in AUDIO_FOLDER.iterdir():

        if audio_file.suffix.lower() not in {
            ".mp3",
            ".m4a",
            ".wav",
        }:
            continue

        try:
            chapter_number = int(
                audio_file.stem.replace(
                    "chapter_",
                    "",
                )
            )

            audio_files[chapter_number] = audio_file

        except ValueError:
            continue
# =============================================================================
# AUDIOBOOK
# =============================================================================

for chapter_number, chapter_title in TWILIGHT_CHAPTERS.items():

    audio_file = audio_files.get(
        chapter_number
    )

    # -------------------------------------------------------------------------
    # Chapter Status
    # -------------------------------------------------------------------------

    if audio_file:
        status = ""
        card_class = "chapter-card chapter-card-recorded"

    else:
        status = """
<div class="chapter-status">
Not recorded yet
</div>
"""
        card_class = "chapter-card"

    # -------------------------------------------------------------------------
    # Chapter Card
    # -------------------------------------------------------------------------

    st.markdown(
        f"""
<div class="{card_class}">
<div class="chapter-number">CHAPTER {chapter_number:02d}</div>
<div class="chapter-title">{chapter_title}</div>
{status}
</div>
""",
        unsafe_allow_html=True,
    )

    # -------------------------------------------------------------------------
    # Audio Player
    # -------------------------------------------------------------------------

    if audio_file:
        st.audio(
            str(audio_file)
        )