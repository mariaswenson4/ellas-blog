import streamlit as st


def apply_base_styles():
    """
    Global styling used across the entire website.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           SHRINK STREAMLIT HEADER INSTEAD OF REMOVING IT
           ========================================================= */

        [data-testid="stHeader"] {
            height: 3rem !important;
            background: transparent !important;
        }

        /* Keep Streamlit's sidebar collapse/expand control available */
        [data-testid="stSidebarCollapsedControl"] {
            display: flex !important;
            visibility: visible !important;
        }


        /* =========================================================
           HIDE UNNECESSARY STREAMLIT CHROME
           ========================================================= */

        [data-testid="stToolbar"] {
            display: none !important;
        }

        [data-testid="stDecoration"] {
            display: none !important;
        }


        /* =========================================================
           REDUCE TOP PAGE SPACING
           ========================================================= */

        .block-container {
            padding-top: 0 !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )