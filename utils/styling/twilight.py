
import streamlit as st


# =============================================================================
# TWILIGHT PAGE STYLING
# =============================================================================

def apply_twilight_styles():
    """
    Apply Twilight-specific styling.

    Background images are handled separately by render_background().
    Headers use the shared render_page_header() component.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           PAGE LAYOUT
           ========================================================= */

        .stApp {
            color: #f1eee6;
        }

        .block-container {
            max-width: 900px;
            padding-top: 4rem;
            padding-bottom: 6rem;
        }


        /* =========================================================
   TWILIGHT HEADER THEME
   ========================================================= */

        .site-page-header.theme-twilight {
            text-align: center !important;
            margin: 20px auto 60px !important;
        }

        .site-page-header.theme-twilight .site-header-eyebrow {
            font-size: 0.75rem !important;
            font-weight: 700;
            letter-spacing: 4px;
            color: #c1cbc4 !important;
            margin-bottom: 12px;
        }

        .site-page-header.theme-twilight .site-header-title {
            font-family: Georgia, serif !important;
            font-size: 5rem !important;
            font-weight: 400 !important;
            letter-spacing: 5px;
            line-height: 1.1;
            color: #ffffff !important;
            margin-bottom: 18px;
        }

        .site-page-header.theme-twilight .site-header-subtitle {
            max-width: 550px;
            margin: 0 auto;
            font-family: Georgia, serif !important;
            font-size: 1rem !important;
            font-style: italic !important;
            line-height: 1.6;
            color: #d3dad5 !important;
        }

        @media (max-width: 800px) {
            .site-page-header.theme-twilight .site-header-title {
                font-size: 3.4rem !important;
            }
        }

        /* =========================================================
           CHAPTER CARDS
           ========================================================= */

        .chapter-card {
            background: rgba(8, 15, 14, 0.72);

            border: 1px solid rgba(255, 255, 255, 0.18);
            border-left: 4px solid rgba(140, 29, 36, 0.90);
            border-radius: 12px;

            padding: 18px 22px;

            margin-top: 18px;
            margin-bottom: 10px;

            backdrop-filter: blur(7px);
            -webkit-backdrop-filter: blur(7px);

            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.22);

            transition:
                background 0.2s ease,
                transform 0.2s ease;
        }

        .chapter-card:hover {
            background: rgba(8, 15, 14, 0.82);
            transform: translateY(-2px);
        }


        /* =========================================================
           CHAPTER INFORMATION
           ========================================================= */

        .chapter-number {
            font-size: 0.7rem;
            font-weight: 800;
            letter-spacing: 3px;

            color: #aebbb2;

            margin-bottom: 5px;
        }

        .chapter-title {
            font-family: Georgia, serif;
            font-size: 1.4rem;
            font-weight: 600;

            color: #ffffff;

            margin-bottom: 6px;

            text-shadow: 0 2px 5px rgba(0, 0, 0, 0.50);
        }

        .chapter-status {
            font-family: Georgia, serif;
            font-size: 0.82rem;
            font-style: italic;

            color: rgba(255, 255, 255, 0.55);
        }


        /* =========================================================
           RECORDED CHAPTERS
           ========================================================= */

        .chapter-card-recorded {
            margin-bottom: 0;
            padding-bottom: 16px;

            border-radius: 12px 12px 0 0;
            border-bottom: none;
        }


        /* =========================================================
           AUDIO PLAYERS
           ========================================================= */

        [data-testid="stAudio"] {
            margin-top: -1px;
            margin-bottom: 25px;
        }

        [data-testid="stAudio"] audio {
            width: 100%;
            border-radius: 0 0 12px 12px;
            background: rgba(8, 15, 14, 0.82);
        }


        /* =========================================================
           EMPTY STATE
           ========================================================= */

        .twilight-empty {
            text-align: center;
            padding: 40px;

            background: rgba(10, 15, 12, 0.78);

            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 10px;

            color: #d0d8d2;

            font-family: Georgia, serif;
            font-style: italic;

            backdrop-filter: blur(6px);
        }


        /* =========================================================
           MOBILE RESPONSIVENESS
           ========================================================= */

        @media (max-width: 800px) {

            .theme-twilight .site-header-title {
                font-size: 3.4rem;
            }

            .theme-twilight .site-header-eyebrow {
                font-size: 0.65rem;
                letter-spacing: 2px;
            }

            .theme-twilight .site-header-subtitle {
                font-size: 0.9rem;
                padding: 0 15px;
            }

            .chapter-card {
                padding: 16px 18px;
            }

            .chapter-title {
                font-size: 1.25rem;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )