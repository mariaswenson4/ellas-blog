import streamlit as st


def apply_base_styles():
    """
    Global styling used across the entire website.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           REMOVE STREAMLIT TOP HEADER
           ========================================================= */

        [data-testid="stHeader"] {
            display: none !important;
        }

        header[data-testid="stHeader"] {
            height: 0 !important;
        }


        /* =========================================================
           REMOVE SPACE AT TOP OF PAGE
           ========================================================= */

        .block-container {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }

        [data-testid="stAppViewContainer"] > .main {
            padding-top: 0 !important;
        }


        /* =========================================================
           REMOVE STREAMLIT TOOLBAR / MENU
           ========================================================= */

        [data-testid="stToolbar"] {
            display: none !important;
        }

        [data-testid="stDecoration"] {
            display: none !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )