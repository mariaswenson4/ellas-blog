from pathlib import Path
import base64

import streamlit as st


# =============================================================================
# Image Helper
# =============================================================================

def _image_to_base64(image_path: str) -> str:
    """Convert an image to base64 so it can be used in CSS."""

    path = Path(image_path)

    if not path.exists():
        return ""

    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")

    return f"data:image/jpeg;base64,{encoded}"


# =============================================================================
# South Park Styles
# =============================================================================

def apply_southpark_styles():
    """Apply styling used only on the South Park page."""

    background = _image_to_base64(
        "images/southparkbackground.jpg"
    )

    st.markdown(
        f"""
        <style>
        /* =========================================================
   RATING BADGES
   ========================================================= */

.rating-badge {{
    display: inline-flex;
    align-items: center;
    justify-content: center;

    min-width: 58px;
    height: 34px;

    padding: 0 12px;

    border: 3px solid #111111;
    border-radius: 999px;

    color: white;

    font-size: 0.95rem;
    font-weight: 900;

    box-shadow: 3px 3px 0 #111111;

    text-shadow:
        1px 1px 1px rgba(0, 0, 0, 0.45);
}}
        /* =========================================================
           PAGE BACKGROUND
           ========================================================= */

        .stApp {{
            background-image:
                linear-gradient(
                    rgba(0, 0, 0, 0.10),
                    rgba(0, 0, 0, 0.10)
                ),
                url("{background}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}


        /* =========================================================
           MAIN CONTENT AREA
           ========================================================= */

        .block-container {{
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }}


        /* =========================================================
           SOUTH PARK TITLE
           ========================================================= */

        .southpark-title {{
            text-align: center;

            font-size: 3rem;
            font-weight: 900;

            color: #111111;

            margin-bottom: 5px;

            text-shadow:
                2px 2px 0 rgba(255, 255, 255, 0.75);
        }}


        .southpark-subtitle {{
            text-align: center;

            font-size: 1.1rem;

            color: #333333;

            margin-bottom: 30px;
        }}


        /* =========================================================
           SEASON HEADING
           ========================================================= */

        .season-heading {{
            text-align: center;

            font-size: 2.4rem;
            font-weight: 900;

            color: #f4d35e;

            margin-top: 20px;
            margin-bottom: 25px;

            text-shadow:
                2px 2px 0 #111111;
        }}


        /* =========================================================
           SELECT BOX
           ========================================================= */

        [data-testid="stSelectbox"] {{
            max-width: 400px;

            margin-left: auto;
            margin-right: auto;
        }}


        /* =========================================================
           EPISODE BUTTONS
           ========================================================= */

        .stButton > button {{
            background:
                rgba(255, 255, 255, 0.94);

            color:
                #111111;

            border:
                3px solid #111111;

            border-radius:
                10px;

            font-weight:
                800;

            text-align:
                left;

            box-shadow:
                4px 4px 0 #111111;

            transition:
                transform 0.1s ease,
                box-shadow 0.1s ease;
        }}


        .stButton > button:hover {{
            background:
                #f4d35e;

            color:
                #111111;

            border-color:
                #111111;

            transform:
                translate(-2px, -2px);

            box-shadow:
                6px 6px 0 #111111;
        }}


        .stButton > button:active {{
            transform:
                translate(2px, 2px);

            box-shadow:
                1px 1px 0 #111111;
        }}


        /* =========================================================
           EPISODE DETAIL CARD
           ========================================================= */

        .episode-detail-card {{
            max-width:
                750px;

            margin:
                30px auto;

            padding:
                40px;

            background:
                rgba(255, 255, 255, 0.95);

            border:
                4px solid #111111;

            border-radius:
                16px;

            box-shadow:
                8px 8px 0 rgba(0, 0, 0, 0.75);

            color:
                #111111;
        }}


        /* =========================================================
           EPISODE LABEL
           ========================================================= */

        .episode-label {{
            text-align:
                center;

            font-size:
                0.9rem;

            font-weight:
                800;

            letter-spacing:
                2px;

            margin-bottom:
                10px;
        }}


        /* =========================================================
           EPISODE TITLE
           ========================================================= */

        .episode-detail-title {{
            text-align:
                center;

            font-size:
                2.3rem;

            font-weight:
                900;

            line-height:
                1.1;

            margin-bottom:
                15px;
        }}


        /* =========================================================
           RATING
           ========================================================= */

        .episode-rating {{
            text-align:
                center;

            font-size:
                1.8rem;

            font-weight:
                900;

            margin-bottom:
                30px;
        }}


        /* =========================================================
           EPISODE INFORMATION
           ========================================================= */

        .episode-info {{
            font-size:
                1rem;

            margin:
                8px 0;
        }}

        /* =========================================================
   STATS
   ========================================================= */

.stats-heading {{
    text-align: center;

    font-size: 2.5rem;
    font-weight: 900;

    color: #f4d35e;

    margin-top: 70px;
    margin-bottom: 25px;

    text-shadow:
        2px 2px 0 #111111;
}}


.stat-card {{
    background:
        rgba(255, 255, 255, 0.94);

    border:
        4px solid #111111;

    border-radius:
        14px;

    padding:
        24px 15px;

    text-align:
        center;

    color:
        #111111;

    box-shadow:
        6px 6px 0 #111111;

    height:
        135px;
    
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.character-row {{
    display: flex;
    align-items: center;
    gap: 15px;

    margin-bottom: 14px;

    background: rgba(255, 255, 255, 0.94);

    border: 3px solid #111111;
    border-radius: 12px;

    padding: 10px 15px;

    box-shadow: 4px 4px 0 #111111;
}}


.character-picture {{
    width: 65px;
    height: 65px;

    flex-shrink: 0;

    display: flex;
    align-items: center;
    justify-content: center;
}}


.character-image {{
    max-width: 65px;
    max-height: 65px;

    object-fit: contain;
}}


.character-placeholder {{
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
}}


.character-content {{
    flex: 1;
}}


.character-name {{
    font-size: 1rem;
    font-weight: 900;

    color: #111111;

    margin-bottom: 7px;
}}


.character-bar-area {{
    position: relative;

    width: 100%;
    height: 25px;

    background: #eeeeee;

    border: 2px solid #111111;
    border-radius: 999px;

    overflow: hidden;
}}


.character-bar {{
    height: 100%;

    background: #f4d35e;

    border-right: 2px solid #111111;

    min-width: 8px;
}}


.character-count {{
    position: absolute;

    right: 9px;
    top: 50%;

    transform: translateY(-50%);

    font-size: 0.85rem;
    font-weight: 900;

    color: #111111;
}}


.stat-label {{
    font-size:
        0.85rem;

    font-weight:
        900;

    letter-spacing:
        1.5px;

    margin-bottom:
        8px;
}}


.stat-number {{
    font-size:
        2rem;

    font-weight:
        900;
}}


.stat-small {{
    font-size:
        0.9rem;

    font-weight:
        700;

    margin-top:
        4px;

    color:
        #555555;
}}


.character-heading {{
    text-align:
        center;

    font-size:
        1.4rem;

    font-weight:
        900;

    letter-spacing:
        1.5px;

    margin-top:
        45px;

    margin-bottom:
        15px;

    color:
        #f4d35e;

    text-shadow:
        1px 1px 0 #111111;
}}


.no-stats {{
    text-align:
        center;

    background:
        rgba(255, 255, 255, 0.92);

    border:
        3px solid #111111;

    border-radius:
        10px;

    padding:
        20px;

    color:
        #111111;

    font-weight:
        700;
}}


        /* =========================================================
           COMMENTS
           ========================================================= */

        .episode-comments-title {{
            margin-top:
                30px;

            margin-bottom:
                8px;

            font-size:
                0.9rem;

            font-weight:
                900;

            letter-spacing:
                2px;
        }}


        .episode-comments {{
            font-size:
                1.05rem;

            line-height:
                1.6;
        }}


        /* =========================================================
           MOBILE / SMALL SCREENS
           ========================================================= */

        @media (max-width: 700px) {{

            .block-container {{
                padding-left: 1rem;
                padding-right: 1rem;
            }}

            .southpark-title {{
                font-size: 2.2rem;
            }}

            .season-heading {{
                font-size: 1.9rem;
            }}

            .episode-detail-card {{
                padding: 25px;
            }}

            .episode-detail-title {{
                font-size: 1.8rem;
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )