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
           Keep it functional but overlay it on the page
           ========================================================= */

        header[data-testid="stHeader"] {
            background: transparent !important;
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            z-index: 999999 !important;
        }


        /* =========================================================
           HIDE ONLY THE TOP-RIGHT STREAMLIT TOOLBAR
           ========================================================= */

        [data-testid="stToolbar"] {
            display: none !important;
        }

        [data-testid="stDecoration"] {
            display: none !important;
        }


        /* =========================================================
           KEEP SIDEBAR BUTTON ABOVE EVERYTHING
           ========================================================= */

        [data-testid="stSidebarCollapsedControl"] {
            position: fixed !important;
            top: 10px !important;
            left: 10px !important;

            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;

            z-index: 1000000 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )