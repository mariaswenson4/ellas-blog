from pathlib import Path
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent
LOGO_PATH = PROJECT_ROOT / "images" / "logo.jpg"

st.set_page_config(
    page_title="Ella's Super Hot Fantastic Blog that Maria Made for Her",
    page_icon=str(LOGO_PATH),
    layout="wide",
)