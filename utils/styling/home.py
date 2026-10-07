from pathlib import Path
import base64

import streamlit as st
from utils.styling.base import apply_base_styles
# =============================================================================
# IMAGE HELPER
# =============================================================================

def _image_to_base64(image_path: str) -> str:

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
# HOME STYLES
# =============================================================================
def apply_home_styles():

    apply_base_styles()

    project_root = (
        Path(__file__)
        .resolve()
        .parent
        .parent
        .parent
    )

    background_path = (
        project_root
        / "images"
        / "homebackground.png"
    )

    background = _image_to_base64(
        str(background_path)
    )

    st.markdown(
        f"""
<style>

/* ============================================================
   PAGE BACKGROUND
   ============================================================ */

.stApp {{
    background-image:
        linear-gradient(
            rgba(20, 12, 30, 0.30),
            rgba(10, 8, 18, 0.48)
        ),
        url("{background}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}


/* ============================================================
   MAIN CONTENT
   ============================================================ */

[data-testid="stMainBlockContainer"] {{
    max-width: 1200px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}}


/* ============================================================
   HERO
   ============================================================ */

.home-hero {{
    text-align: center;

    max-width: 850px;

    margin:
        20px auto
        65px auto;

    padding:
        42px
        35px;

    background:
        rgba(25, 18, 35, 0.72);

    border:
        1px solid
        rgba(255, 255, 255, 0.18);

    border-radius: 24px;

    backdrop-filter: blur(8px);

    -webkit-backdrop-filter:
        blur(8px);

    box-shadow:
        0 15px 45px
        rgba(0, 0, 0, 0.30);
}}


.home-eyebrow {{
    font-size: 0.72rem;

    font-weight: 800;

    letter-spacing: 5px;

    color: #d8bddf;

    margin-bottom: 14px;
}}


.home-title {{
    font-family:
        Georgia,
        serif;

    font-size: 4rem;

    line-height: 1.02;

    font-weight: 700;

    color: #ffffff;

    text-shadow:
        0 3px 12px
        rgba(0, 0, 0, 0.50);

    margin-bottom: 20px;
}}


.home-subtitle {{
    max-width: 650px;

    margin: auto;

    font-family:
        Georgia,
        serif;

    font-size: 1.05rem;

    font-style: italic;

    line-height: 1.7;

    color:
        rgba(255, 255, 255, 0.82);
}}


/* ============================================================
   SECTION TITLE
   ============================================================ */

.home-section-title {{
    text-align: center;

    font-size: 0.75rem;

    font-weight: 800;

    letter-spacing: 5px;

    color: #ffffff;

    margin-bottom: 28px;

    text-shadow:
        0 2px 6px
        rgba(0, 0, 0, 0.8);
}}


/* ============================================================
   CARDS
   ============================================================ */

.home-card {{
    min-height: 205px;

    padding: 25px;

    background:
        rgba(20, 17, 28, 0.78);

    border:
        1px solid
        rgba(255, 255, 255, 0.17);

    border-radius: 18px;

    backdrop-filter:
        blur(8px);

    -webkit-backdrop-filter:
        blur(8px);

    box-shadow:
        0 10px 30px
        rgba(0, 0, 0, 0.25);

    transition:
        transform 0.2s ease,
        background 0.2s ease;
}}


.home-card:hover {{
    transform:
        translateY(-4px);

    background:
        rgba(30, 22, 40, 0.88);
}}


.home-card-small {{
    font-size: 0.62rem;

    font-weight: 800;

    letter-spacing: 3px;

    color: #cdb2d8;

    margin-bottom: 12px;
}}


.home-card-title {{
    font-family:
        Georgia,
        serif;

    font-size: 1.7rem;

    font-weight: 700;

    color: #ffffff;

    margin-bottom: 12px;
}}


.home-card-description {{
    font-size: 0.92rem;

    line-height: 1.65;

    color:
        rgba(255, 255, 255, 0.72);
}}


/* ============================================================
   BUTTONS
   ============================================================ */

.stButton > button {{
    background:
        rgba(52, 35, 65, 0.90);

    color: white;

    border:
        1px solid
        rgba(255, 255, 255, 0.20);

    border-radius: 10px;

    font-weight: 700;

    transition:
        all 0.2s ease;
}}


.stButton > button:hover {{
    background:
        rgba(89, 59, 105, 0.95);

    border-color:
        rgba(255, 255, 255, 0.40);

    transform:
        translateY(-2px);
}}


/* ============================================================
   FOOTER
   ============================================================ */

.home-footer {{
    text-align: center;

    margin-top: 75px;

    padding: 25px;

    font-family:
        Georgia,
        serif;

    font-size: 0.9rem;

    font-style: italic;

    color:
        rgba(255, 255, 255, 0.65);

    text-shadow:
        0 2px 5px
        rgba(0, 0, 0, 0.8);
}}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 800px) {{

    .home-title {{
        font-size: 2.7rem;
    }}

    .home-hero {{
        padding:
            32px
            20px;

        margin-bottom:
            45px;
    }}

}}

</style>
""",
        unsafe_allow_html=True,
    )