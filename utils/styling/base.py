import streamlit as st


def apply_base_styles():
    """
    Global styling used across the entire website.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           MAKE STREAMLIT HEADER COMPLETELY TRANSPARENT
           ========================================================= */

        header[data-testid="stHeader"],
        [data-testid="stHeader"],
        [data-testid="stHeader"] > div {
            background: transparent !important;
            background-color: transparent !important;
        }


        /* =========================================================
           MAKE HEADER FLOAT OVER PAGE
           ========================================================= */

        header[data-testid="stHeader"] {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;

            height: 3rem !important;

            z-index: 999999 !important;

            pointer-events: none !important;
        }


        /* =========================================================
           KEEP SIDEBAR BUTTON CLICKABLE
           ========================================================= */

        [data-testid="stSidebarCollapsedControl"] {
            position: fixed !important;

            top: 10px !important;
            left: 10px !important;

            display: flex !important;
            visibility: visible !important;
            opacity: 1 !important;

            z-index: 1000000 !important;

            pointer-events: auto !important;
        }


        /* =========================================================
           HIDE STREAMLIT TOOLBAR / MENU
           ========================================================= */

        [data-testid="stToolbar"] {
            display: none !important;
        }

        [data-testid="stDecoration"] {
            display: none !important;
        }


        /* =========================================================
           REMOVE HEADER SPACE
           ========================================================= */

        [data-testid="stAppViewContainer"] {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }

        [data-testid="stMain"] {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )