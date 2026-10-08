
import base64
from pathlib import Path

import streamlit as st


# =============================================================================
# BACKGROUND HELPER
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def render_background(
    image_name: str,
    overlay: float = 0.2,
    position: str = "center",
    size: str = "cover",
    attachment: str = "fixed",
):
    """Apply a background image to the current Streamlit page."""

    image_path = PROJECT_ROOT / "images" / image_name

    if not image_path.is_file():
        st.warning(f"Background not found: {image_name}")
        return

    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }

    mime = mime_types.get(
        image_path.suffix.lower(),
        "image/jpeg",
    )

    encoded = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    background = f"data:{mime};base64,{encoded}"
    overlay = max(0.0, min(1.0, overlay))

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0, 0, 0, {overlay}),
                    rgba(0, 0, 0, {overlay})
                ),
                url("{background}");

            background-size: {size};
            background-position: {position};
            background-repeat: no-repeat;
            background-attachment: {attachment};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
