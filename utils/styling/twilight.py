from pathlib import Path
import base64

import streamlit as st


# =============================================================================
# IMAGE HELPER
# =============================================================================

def _image_to_base64(image_path: str) -> str:
    """Convert an image to a base64 data URI."""

    path = Path(image_path)

    if not path.exists():
        return ""

    suffix = path.suffix.lower()

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }

    mime_type = mime_types.get(
        suffix,
        "image/jpeg",
    )

    encoded = base64.b64encode(
        path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


# =============================================================================
# TWILIGHT STYLES
# =============================================================================

def apply_twilight_styles():

    background = _image_to_base64(
        "images/twilightbackground.jpg"
        
    )

    st.markdown(
        f"""
<style>

/* =========================================================
   PAGE BACKGROUND
   ========================================================= */

.stApp {{
    background-image:
        linear-gradient(
            rgba(5, 10, 8, 0.50),
            rgba(5, 10, 8, 0.72)
        ),
        url("{background}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;

    color: #f1eee6;
}}


.block-container {{
    max-width: 900px;

    padding-top: 4rem;
    padding-bottom: 6rem;
}}


/* =========================================================
   HEADER
   ========================================================= */

.twilight-header {{
    text-align: center;

    margin-bottom: 60px;
}}


.twilight-eyebrow {{
    font-size: 0.75rem;
    font-weight: 700;

    letter-spacing: 4px;

    color: #c1cbc4;

    margin-bottom: 12px;
}}


.twilight-title {{
    font-family: Georgia, serif;

    font-size: 5rem;
    font-weight: 400;

    letter-spacing: 5px;

    color: #ffffff;

    line-height: 1;
}}


.twilight-subtitle {{
    max-width: 550px;

    margin: 18px auto 0 auto;

    font-family: Georgia, serif;

    font-size: 1rem;
    font-style: italic;

    line-height: 1.6;

    color: #d3dad5;
}}


/* =========================================================
   CHAPTERS
   ========================================================= */

.chapter-heading {{
    margin-top: 35px;
    margin-bottom: 10px;

    padding: 20px 22px;

    background: rgba(10, 15, 12, 0.82);

    border: 1px solid rgba(255, 255, 255, 0.15);

    border-left: 4px solid #8c1d24;

    border-radius: 0 10px 10px 0;

    backdrop-filter: blur(6px);
}}
.chapter-card {{
    background: rgba(8, 15, 14, 0.72);

    border: 1px solid rgba(255, 255, 255, 0.18);

    border-left: 4px solid rgba(140, 29, 36, 0.90);

    border-radius: 12px;

    padding: 18px 22px;

    margin-top: 18px;
    margin-bottom: 10px;

    backdrop-filter: blur(7px);
    -webkit-backdrop-filter: blur(7px);

    box-shadow:
        0 6px 20px rgba(0, 0, 0, 0.22);

    transition:
        background 0.2s ease,
        transform 0.2s ease;
}}


.chapter-card:hover {{
    background: rgba(8, 15, 14, 0.82);

    transform: translateY(-2px);
}}


.chapter-number {{
    font-size: 0.68rem;

    font-weight: 800;

    letter-spacing: 4px;

    color: rgba(255, 255, 255, 0.70);

    margin-bottom: 6px;
}}


.chapter-title {{
    font-family: Georgia, serif;

    font-size: 1.45rem;

    font-weight: 600;

    color: #ffffff;

    margin-bottom: 6px;

    text-shadow:
        0 2px 5px rgba(0, 0, 0, 0.50);
}}


.chapter-status {{
    font-family: Georgia, serif;

    font-size: 0.82rem;

    font-style: italic;

    color: rgba(255, 255, 255, 0.55);
}}


.chapter-status.recorded {{
    color: #c4d6ca;

    font-family: inherit;

    font-style: normal;

    font-size: 0.65rem;

    font-weight: 800;

    letter-spacing: 2px;
}}

.chapter-number {{
    font-size: 0.7rem;
    font-weight: 800;

    letter-spacing: 3px;

    color: #aebbb2;

    margin-bottom: 5px;
}}


.chapter-title {{
    font-family: Georgia, serif;

    font-size: 1.4rem;

    color: #ffffff;
}}


/* =========================================================
   EMPTY STATE
   ========================================================= */

.twilight-empty {{
    text-align: center;

    padding: 40px;

    background: rgba(10, 15, 12, 0.78);

    border: 1px solid rgba(255, 255, 255, 0.18);

    border-radius: 10px;

    color: #d0d8d2;

    font-family: Georgia, serif;

    font-style: italic;

    backdrop-filter: blur(6px);
}}
/* =========================================================
   AUDIO PLAYER
   ========================================================= */

[data-testid="stAudio"] {{
    margin-top: -11px;
    margin-bottom: 24px;
}}


/* Audio player itself */

[data-testid="stAudio"] audio {{
    width: 100%;

    border-radius: 0 0 12px 12px;

    background: rgba(8, 15, 14, 0.82);
}}

.chapter-card-recorded {{
    margin-bottom: 0;

    padding-bottom: 16px;

    border-radius: 12px 12px 0 0;

    border-bottom: none;
}}


[data-testid="stAudio"] {{
    margin-top: -1px;
    margin-bottom: 48px;
}}


[data-testid="stAudio"] audio {{
    width: 100%;

    border-radius: 0 0 12px 12px;
}}
/* =========================================================
   AUDIO PLAYER
   ========================================================= */

[data-testid="stAudio"] {{
    margin-bottom: 25px;
}}

</style>
""",
        unsafe_allow_html=True,
    )