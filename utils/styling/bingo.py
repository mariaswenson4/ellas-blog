
import streamlit as st


def apply_bingo_styles():

    st.markdown(
        """
<style>

/* =========================================================
   MAIN PAGE LAYOUT
   ========================================================= */

.stMainBlockContainer {
    max-width: 850px !important;
    padding-top: 3rem !important;
    padding-bottom: 5rem !important;
}


/* =========================================================
   PAGE HEADER
   ========================================================= */

.site-page-header.them-bingo {
    text-align: center;
    margin-bottom: 3rem;
}

.site-page-header.them-bingo .site-header-eyebrow {
    color: #E5C99F;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.site-page-header.them-bingo .site-header-title {
    font-family: Georgia, serif;
    font-size: clamp(3rem, 7vw, 4.5rem);
    font-weight: 700;
    color: #FFFFFF;
    text-shadow: 0 4px 18px rgba(0,0,0,0.7);
    margin-bottom: 12px;
}

.site-page-header.them-bingo .site-header-subtitle {
    font-family: Georgia, serif;
    font-size: 17px;
    font-style: italic;
    color: #FFF0DE;
    text-shadow: 0 2px 8px rgba(0,0,0,0.8);
}


/* =========================================================
   MAIN CARDS
   ========================================================= */

.st-key-bingo_form_card,
.st-key-bingo_history_card {
    background: rgba(14, 20, 19, 0.93) !important;
    border: 1px solid rgba(255,255,255,0.17) !important;
    border-left: 3px solid #D99532 !important;
    border-radius: 14px !important;
    padding: 26px !important;
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 35px rgba(0,0,0,0.35);
}


/* =========================================================
   CARD HEADINGS
   ========================================================= */

.st-key-bingo_form_card h3,
.st-key-bingo_history_card h3 {
    font-family: Georgia, serif !important;
    font-size: 1.7rem !important;
    color: #FFF4E8 !important;
    margin-bottom: 0 !important;
}

.st-key-bingo_form_card [data-testid="stCaptionContainer"],
.st-key-bingo_history_card [data-testid="stCaptionContainer"] {
    color: #BDAFA4 !important;
    font-size: 13px !important;
}


/* =========================================================
   REMOVE INNER FORM BORDER
   ========================================================= */

.st-key-bingo_form_card [data-testid="stForm"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* =========================================================
   BINGO RULES CARD
   ========================================================= */

.bingo-rules-card {
    background: rgba(14, 20, 19, 0.93);
    border: 1px solid rgba(255,255,255,0.17);
    border-left: 3px solid #D99532;
    border-radius: 14px;
    padding: 28px;
    margin-bottom: 28px;
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 35px rgba(0,0,0,0.35);
}

.bingo-rules-eyebrow {
    color: #D99532;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-bottom: 6px;
}

.bingo-rules-title {
    font-family: Georgia, serif;
    color: #FFF4E8;
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 24px;
}

.bingo-rule {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 20px;
}

.bingo-rule-number {
    background: rgba(217,149,50,0.15);
    color: #D99532;
    padding: 9px 12px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 700;
}

.bingo-rule strong {
    color: #FFF4E8;
    font-size: 15px;
}

.bingo-rule p {
    color: #C9C2B9;
    font-size: 13px;
    line-height: 1.6;
    margin: 5px 0 0;
}

.bingo-rules-footer {
    background: rgba(217,149,50,0.10);
    color: #E8C58D;
    padding: 14px;
    border-radius: 8px;
    font-size: 13px;
    font-style: italic;
    text-align: center;
}

@media (max-width: 640px) {
    .bingo-rules-card {
        padding: 20px;
    }
}



/* =========================================================
   INPUT LABELS
   ========================================================= */

.st-key-bingo_form_card [data-testid="stWidgetLabel"] {
    color: #F5E9DF !important;
    font-weight: 500 !important;
}


/* =========================================================
   INPUT FIELDS
   ========================================================= */

.st-key-bingo_form_card [data-baseweb="input"] > div,
.st-key-bingo_form_card [data-baseweb="select"] > div {
    background: #303432 !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 8px !important;
}


/* =========================================================
   SAVE BUTTON
   ========================================================= */

/* =========================================================
   SAVE BUTTON — GOLDEN ORANGE
   ========================================================= */

.st-key-bingo_form_card [data-testid="stFormSubmitButton"] button {
    background: #D99532 !important;
    color: #1A1A1A !important;
    border: none !important;
    border-radius: 8px !important;
    min-height: 44px !important;
    font-weight: 700 !important;
    transition: background 0.2s ease;
}

.st-key-bingo_form_card [data-testid="stFormSubmitButton"] button:hover {
    background: #EAB052 !important;
    color: #1A1A1A !important;
    border: none !important;
}


/* =========================================================
   BINGO HISTORY TABLE
   ========================================================= */

.st-key-bingo_history_card [data-testid="stDataFrame"] {
    border-radius: 10px !important;
    overflow: hidden;
}


/* =========================================================
   MOBILE RESPONSIVENESS
   ========================================================= */

@media (max-width: 640px) {

    .stMainBlockContainer {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    .st-key-bingo_form_card,
    .st-key-bingo_history_card {
        padding: 18px !important;
    }

    .site-page-header.them-bingo .site-header-title {
        font-size: 2.7rem !important;
    }
}

/* =========================================================
   BINGO STATISTICS CARD
   ========================================================= */

.st-key-bingo_stats_card {
    background: rgba(14, 20, 19, 0.93) !important;
    border: 1px solid rgba(255,255,255,0.17) !important;
    border-left: 3px solid #D99532 !important;
    border-radius: 14px !important;
    padding: 26px !important;
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 35px rgba(0,0,0,0.35);
}

.st-key-bingo_stats_card h3 {
    font-family: Georgia, serif !important;
    font-size: 1.7rem !important;
    color: #FFF4E8 !important;
}

.st-key-bingo_stats_card h4 {
    font-family: Georgia, serif !important;
    color: #FFF4E8 !important;
}

/* Metric cards */

.st-key-bingo_stats_card [data-testid="stMetric"] {
    background: rgba(217,149,50,0.08);
    border: 1px solid rgba(217,149,50,0.25);
    border-radius: 12px;
    padding: 18px;
    text-align: center;
}

.st-key-bingo_stats_card [data-testid="stMetricValue"] {
    color: #D99532 !important;
    font-family: Georgia, serif;
    font-size: 2.4rem !important;
}

.st-key-bingo_stats_card [data-testid="stMetricLabel"] {
    color: #E8D6C0 !important;
}

@media (max-width: 640px) {
    .st-key-bingo_stats_card {
        padding: 18px !important;
    }
}


</style>
        """,
        unsafe_allow_html=True
    )
