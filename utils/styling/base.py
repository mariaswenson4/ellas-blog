import streamlit as st


def apply_base_styles():
    """
    Global styling used across the entire website.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           STREAMLIT HEADER
           Keep normal functionality, just make it transparent
           ========================================================= */

        [data-testid="stHeader"] {
            background: transparent !important;
        }


        /* =========================================================
           REMOVE STREAMLIT DECORATION LINE
           ========================================================= */

        [data-testid="stDecoration"] {
            display: none !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )