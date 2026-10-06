from pathlib import Path
import base64

import streamlit as st


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
        / "homebackground.jpg"
    )

    background = _image_to_base64(
        str(background_path)
    )

    st.markdown(
        f"""
<style>

.stApp {{
    background-image:
        linear-gradient(
            rgba(0, 0, 0, 0.25),
            rgba(0, 0, 0, 0.35)
        ),
        url("{background}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

</style>
""",
        unsafe_allow_html=True,
    )