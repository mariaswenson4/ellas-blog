
import streamlit as st


def apply_southpark_styles():
    """Apply South Park-specific styling."""

    st.markdown(
        """
        <style>

        /* =====================================================
           PAGE LAYOUT
           ===================================================== */

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        /* =====================================================
           REUSABLE HEADER THEME
           ===================================================== */

        .theme-southpark.site-page-header {
            text-align: center;
            margin: 10px auto 30px;
        }

        .theme-southpark .site-header-title {
            font-family: inherit;
            font-size: 3rem;
            font-weight: 900;
            color: #111111;
            text-shadow: 2px 2px 0 rgba(255,255,255,.75);
            margin-bottom: 5px;
        }

        .theme-southpark .site-header-subtitle {
            font-family: inherit;
            font-size: 1.1rem;
            font-style: normal;
            color: #333333;
            max-width: 750px;
        }

        .theme-southpark .site-section-title {
            font-family: inherit;
            font-size: 2.5rem;
            font-weight: 900;
            color: #f4d35e;
            text-shadow: 2px 2px 0 #111111;
        }

        /* =====================================================
           SECTION HEADINGS
           ===================================================== */

        .season-heading,
        .character-heading {
            text-align: center;
            font-weight: 900;
            color: #f4d35e;
            text-shadow: 2px 2px 0 #111111;
        }

        .season-heading {
            font-size: 2.4rem;
            margin: 20px 0 25px;
        }

        .character-heading {
            font-size: 1.4rem;
            letter-spacing: 1.5px;
            margin: 45px 0 15px;
        }

        /* =====================================================
           SEASON SELECTOR AND BUTTONS
           ===================================================== */

        [data-testid="stSelectbox"] {
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
        }

        .stButton > button {
            background: rgba(255,255,255,.94);
            color: #111111;
            border: 3px solid #111111;
            border-radius: 10px;
            font-weight: 800;
            text-align: left;
            box-shadow: 4px 4px 0 #111111;
            transition: transform .1s ease, box-shadow .1s ease;
        }

        .stButton > button:hover {
            background: #f4d35e;
            color: #111111;
            border-color: #111111;
            transform: translate(-2px,-2px);
            box-shadow: 6px 6px 0 #111111;
        }

        .stButton > button:active {
            transform: translate(2px,2px);
            box-shadow: 1px 1px 0 #111111;
        }

        /* =====================================================
           RATING BADGES
           ===================================================== */

        .rating-wrapper,
        .detail-rating-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .rating-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 58px;
            height: 34px;
            padding: 0 12px;
            border: 3px solid #111111;
            border-radius: 999px;
            color: white;
            font-size: .95rem;
            font-weight: 900;
            box-shadow: 3px 3px 0 #111111;
            text-shadow: 1px 1px 1px rgba(0,0,0,.45);
        }

        .rating-unrated {
            background: #777777;
        }

        .detail-rating-badge {
            margin-bottom: 22px;
        }

        /* =====================================================
           EPISODE DETAIL CARD
           ===================================================== */

        .episode-detail-card {
            max-width: 750px;
            margin: 30px auto;
            padding: 40px;
            background: rgba(255,255,255,.95);
            border: 4px solid #111111;
            border-radius: 16px;
            box-shadow: 8px 8px 0 rgba(0,0,0,.75);
            color: #111111;
        }

        .episode-label {
            text-align: center;
            font-size: .9rem;
            font-weight: 800;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }

        .episode-detail-title {
            text-align: center;
            font-size: 2.3rem;
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 15px;
        }

        .episode-info {
            font-size: 1rem;
            margin: 8px 0;
        }

        .episode-comments-title {
            margin: 30px 0 8px;
            font-size: .9rem;
            font-weight: 900;
            letter-spacing: 2px;
        }

        .episode-comments {
            font-size: 1.05rem;
            line-height: 1.6;
            white-space: pre-wrap;
        }

        /* =====================================================
           STAT CARDS
           ===================================================== */

        .stat-card {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 135px;
            box-sizing: border-box;
            padding: 24px 15px;
            text-align: center;
            background: rgba(255,255,255,.94);
            border: 4px solid #111111;
            border-radius: 14px;
            box-shadow: 6px 6px 0 #111111;
            color: #111111;
        }

        .stat-label {
            font-size: .85rem;
            font-weight: 900;
            letter-spacing: 1.5px;
            margin-bottom: 8px;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 900;
        }

        .stat-small {
            font-size: .9rem;
            font-weight: 700;
            margin-top: 4px;
            color: #555555;
        }

        /* =====================================================
           FAVORITE CHARACTER RANKINGS
           ===================================================== */

        .character-row {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 14px;
            padding: 10px 15px;
            background: rgba(255,255,255,.94);
            border: 3px solid #111111;
            border-radius: 12px;
            box-shadow: 4px 4px 0 #111111;
        }

        .character-picture {
            width: 65px;
            height: 65px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .character-image {
            max-width: 65px;
            max-height: 65px;
            object-fit: contain;
        }

        .character-placeholder {
            width: 52px;
            height: 52px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #f4d35e;
            border: 3px solid #111111;
            border-radius: 50%;
            font-size: 1.5rem;
            font-weight: 900;
            color: #111111;
        }

        .character-content {
            flex: 1;
            min-width: 0;
        }

        .character-name {
            font-size: 1rem;
            font-weight: 900;
            color: #111111;
            margin-bottom: 7px;
        }

        .character-bar-area {
            position: relative;
            width: 100%;
            height: 25px;
            background: #eeeeee;
            border: 2px solid #111111;
            border-radius: 999px;
            overflow: hidden;
        }

        .character-bar {
            height: 100%;
            min-width: 8px;
            background: #f4d35e;
            border-right: 2px solid #111111;
        }

        .character-count {
            position: absolute;
            right: 9px;
            top: 50%;
            transform: translateY(-50%);
            font-size: .85rem;
            font-weight: 900;
            color: #111111;
        }

        .no-stats {
            text-align: center;
            padding: 20px;
            background: rgba(255,255,255,.92);
            border: 3px solid #111111;
            border-radius: 10px;
            color: #111111;
            font-weight: 700;
        }

        /* =====================================================
           MOBILE
           ===================================================== */

        @media (max-width: 700px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .theme-southpark .site-header-title {
                font-size: 2.2rem;
            }

            .theme-southpark .site-section-title {
                font-size: 1.9rem;
            }

            .season-heading {
                font-size: 1.9rem;
            }

            .episode-detail-card {
                padding: 25px;
            }

            .episode-detail-title {
                font-size: 1.8rem;
            }

            .character-row {
                gap: 10px;
                padding: 10px;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
