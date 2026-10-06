from pathlib import Path
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent
LOGO_PATH = PROJECT_ROOT / "images" / "logo.jpg"

st.set_page_config(
    page_title="Ella's Super Hot Fantastic Blog that Maria Made for Her",
    page_icon=str(LOGO_PATH),
    layout="wide",
)
st.logo(str(LOGO_PATH))

pages = {
    "": [
        st.Page("pages/home.py", title="Home", icon=":material/home:"),
    ],
    "For My Girlfriend": [
        st.Page("pages/southpark.py", title="South Park"),
        st.Page("pages/twilight.py", title="Twilight Audiobook"),
        st.Page("pages/blog.py", title="Blog"),
    ],
}

pg = st.navigation(pages)
pg.run()