from pathlib import Path

import streamlit as st

from utils.styling.twilight import apply_twilight_styles
from utils.styling.backgroundhelper import render_background
from utils.styling.headers import apply_header_styles
from utils.styling.components.headers import render_page_header
from utils.styling.components.html import render_html
# =============================================================================
# PAGE STYLING
# =============================================================================

# =============================================================================
# PAGE STYLING
# =============================================================================

apply_header_styles()
apply_twilight_styles()

render_background(
    image_name="twilightbackground.jpg",
    overlay=0.65,
)

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

# =============================================================================
# HEADER
# =============================================================================

# =============================================================================
# HEADER
# =============================================================================

render_page_header(
    title="Twilight",
    eyebrow="Maria's Version of Twilight as an Audiobook",
    subtitle=(
        "Read specifically to my hot girlfriend with the utmost "
        "enjoyment and pleasure for all first time listeners."
    ),
    theme="twilight",
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

    render_html(
        f"""
        <div class="{card_class}">
            <div class="chapter-number">
                CHAPTER {chapter_number:02d}
            </div>
            <div class="chapter-title">
                {chapter_title}
            </div>
            {status}
        </div>
        """
    )

    # -------------------------------------------------------------------------
    # Audio Player
    # -------------------------------------------------------------------------

    if audio_file:
        st.audio(
            str(audio_file)
        )