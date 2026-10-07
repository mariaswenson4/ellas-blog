import streamlit as st


def apply_base_styles():
    """
    Global styling used across the entire website.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           TRANSPARENT STREAMLIT HEADER
           ========================================================= */

        header[data-testid="stHeader"] {
            background: transparent !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        [data-testid="stHeader"] > div {
            background: transparent !important;
        }


        /* =========================================================
           REMOVE STREAMLIT DECORATION
           ========================================================= */

        [data-testid="stDecoration"] {
            display: none !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )