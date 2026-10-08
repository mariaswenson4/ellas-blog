
import streamlit as st


# =============================================================================
# MOVIES PAGE STYLING
# =============================================================================

def apply_movies_styles():
    """
    Apply styling for the Movies page.

    Backgrounds are handled by render_background().
    Headers are handled by the shared header components.
    """

    st.markdown(
        """
        <style>

        /* =========================================================
           PAGE LAYOUT
           ========================================================= */

        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        [data-testid="stAppViewContainer"] {
            background: transparent !important;
        }

        [data-testid="stMainBlockContainer"] {
            max-width: 1250px;
            padding-top: 3rem;
            padding-bottom: 5rem;
        }

        .stApp::before,
        .stApp::after {
            content: none !important;
        }


        /* =========================================================
           MOVIES HEADER THEME
           ========================================================= */

        .site-page-header.theme-movies {
            text-align: center;
            margin: 20px auto 35px;
        }

        .theme-movies .site-header-eyebrow,
        .theme-movies .site-section-eyebrow {
            color: #f7d6ad;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.85);
        }

        .theme-movies .site-header-title,
        .theme-movies .site-section-title {
            font-family: Georgia, serif;
            color: #fff8ed;
            text-shadow: 0 3px 12px rgba(0, 0, 0, 0.85);
        }

        .theme-movies .site-header-subtitle,
        .theme-movies .site-section-description {
            color: #fff1de;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.9);
        }


        /* =========================================================
           MOVIE POSTERS
           ========================================================= */

        .movie-poster-link {
            display: block;
            width: 100%;
            overflow: hidden;
            border-radius: 12px;
            cursor: pointer;
        }

        .clickable-movie-poster {
            display: block;
            width: 100%;
            height: auto;
            border-radius: 12px;

            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);

            transition:
                transform 0.25s ease,
                filter 0.25s ease;
        }

        .movie-poster-link:hover .clickable-movie-poster {
            transform: scale(1.04);
            filter: brightness(1.12);
        }

        .movie-poster-link:hover {
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.5);
        }

        [data-testid="stImage"] img {
            border-radius: 12px;

            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;
        }

        [data-testid="stImage"] img:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 35px rgba(0, 0, 0, 0.5);
        }


        /* =========================================================
           RECENTLY WATCHED & WATCHLIST
           ========================================================= */

        .recent-movie-title,
        .watchlist-title {
            font-family: Georgia, serif;
            font-weight: 700;
            color: #fff8ed;

            margin-top: 8px;
            margin-bottom: 3px;

            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.9);
        }

        .recent-movie-title {
            font-size: 1.05rem;
        }

        .watchlist-title {
            font-size: 0.95rem;
        }

        .recent-movie-year,
        .watchlist-year {
            font-size: 0.75rem;
            color: #f5d8b7;
            margin-bottom: 7px;

            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
        }

        .movie-rating {
            font-size: 0.95rem;
            letter-spacing: 1px;
            color: #ffd28b;
            margin-bottom: 5px;

            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8);
        }

        .movie-date {
            font-size: 0.72rem;
            color: #f1e2d0;

            text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9);
        }


        /* =========================================================
           BUTTONS
           ========================================================= */

        .stButton > button,
        .stLinkButton > a {
            min-height: 44px;

            background: rgba(20, 35, 39, 0.92) !important;
            color: #fff2dc !important;

            border: 1px solid rgba(245, 196, 143, 0.45) !important;
            border-radius: 10px !important;

            font-weight: 700 !important;

            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);

            transition: all 0.2s ease !important;
        }

        .stButton > button:hover,
        .stLinkButton > a:hover {
            background: #b9573d !important;
            color: #fff8ed !important;
            border-color: #e9ad80 !important;

            transform: translateY(-2px);
        }


        /* =========================================================
           DIVIDERS
           ========================================================= */

        hr {
            margin-top: 70px !important;
            margin-bottom: 20px !important;

            border-color: rgba(255, 235, 205, 0.35) !important;
        }


        /* =========================================================
           RANDOMIZER - MATCHING LEFT & RIGHT PANELS
           ========================================================= */

        .st-key-randomizer_left,
        .st-key-randomizer_right {
            background: rgba(16, 29, 33, 0.88);

            border: 1px solid rgba(255, 235, 205, 0.25);
            border-radius: 18px;

            padding: 28px;
            min-height: 340px;

            box-shadow: 0 12px 35px rgba(0, 0, 0, 0.3);

            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }

        /* Center contents vertically */

        .st-key-randomizer_left,
        .st-key-randomizer_right {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }


        /* =========================================================
           LEFT PANEL - CAN'T DECIDE?
           ========================================================= */

        .randomizer-intro {
            text-align: center;

            background: transparent;
            border: none;
            box-shadow: none;

            margin: 0;
            padding: 0;
        }

        .randomizer-eyebrow {
            font-size: 0.65rem;
            font-weight: 800;

            letter-spacing: 3px;
            text-transform: uppercase;

            color: #e9b987;
            margin-bottom: 12px;
        }

        .randomizer-title {
            font-family: Georgia, serif;
            font-size: 2.2rem;
            font-weight: 700;

            color: #fff8ed;
            margin-bottom: 15px;
        }

        .randomizer-description {
            max-width: 400px;
            margin: 0 auto;

            font-family: Georgia, serif;
            font-size: 0.95rem;
            font-style: italic;
            line-height: 1.6;

            color: #e9d9c5;
        }

        /* Space between description and button */

        .st-key-randomizer_left .stButton {
    margin-top: 25px;
    max-width: 320px;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
}
/* =========================================================
   MATERIAL SYMBOLS
   ========================================================= */

.random-placeholder-icon {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 18px;
    color: #f7d6ad;
}

/* Material font ONLY for the movie placeholder */

.random-placeholder-icon .material-symbols-rounded {
    font-family: 'Material Symbols Rounded' !important;
    font-weight: normal;
    font-style: normal;
    font-size: 56px;
    line-height: 1;
    letter-spacing: normal;
    text-transform: none;
    white-space: nowrap;
    font-feature-settings: 'liga';
}
/* Keep regular fonts on Streamlit buttons */

.stButton button,
.stLinkButton a {
    font-family: inherit !important;
}
        /* =========================================================
           RIGHT PANEL - SELECTED MOVIE
           ========================================================= */

        .random-movie-result {
            text-align: center;
            margin-bottom: 18px;
        }

        .random-result-eyebrow {
            font-size: 0.7rem;
            font-weight: 800;

            letter-spacing: 3px;
            text-transform: uppercase;

            color: #f7d6ad;
            margin-bottom: 10px;
        }

        .random-result-title {
            font-family: Georgia, serif;
            font-size: 1.7rem;
            font-weight: 700;

            line-height: 1.3;
            color: #fff8ed;

            text-shadow: 0 3px 10px rgba(0, 0, 0, 0.8);
        }

        /* Center the movie poster */

        .st-key-randomizer_right [data-testid="stImage"] {
            display: flex;
            justify-content: center;

            margin-bottom: 15px;
        }

        .st-key-randomizer_right [data-testid="stImage"] img {
            max-height: 170px;
            width: auto;
            object-fit: contain;
        }

        /* Center the Letterboxd button */

        .st-key-randomizer_right .stLinkButton {
            max-width: 300px;
            width: 100%;
            margin: 0 auto;
        }


        /* =========================================================
           RIGHT PANEL - EMPTY PLACEHOLDER
           ========================================================= */

        .random-movie-placeholder {
            min-height: 240px;
            padding: 15px;

            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            text-align: center;
        }

        .random-placeholder-icon {
            font-size: 2.5rem;
            margin-bottom: 12px;
        }

        .random-placeholder-title {
            font-family: Georgia, serif;
            font-size: 1.7rem;
            font-weight: 700;

            color: #fff8ed;
            margin-bottom: 10px;
        }

        .random-placeholder-description {
            font-family: Georgia, serif;
            font-size: 0.95rem;
            font-style: italic;
            line-height: 1.6;

            color: #f1dfc8;
            max-width: 280px;
        }


        /* =========================================================
           MOBILE RESPONSIVENESS
           ========================================================= */

        @media (max-width: 800px) {

            .theme-movies .site-header-title {
                font-size: 2.7rem;
            }

            .theme-movies .site-section-title {
                font-size: 1.7rem;
            }

            .st-key-randomizer_left,
            .st-key-randomizer_right {
                min-height: auto;
                padding: 25px 20px;
            }

            .randomizer-title {
                font-size: 1.8rem;
            }

            .random-result-title {
                font-size: 1.5rem;
            }

            .random-movie-placeholder {
                min-height: 220px;
            }

            .stApp {
                background-attachment: scroll;
                background-position: center top;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )
