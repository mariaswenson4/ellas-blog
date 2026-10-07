import streamlit as st

from utils.styling.home import apply_home_styles


# =============================================================================
# PAGE STYLING
# =============================================================================

apply_home_styles()


# =================P============================================================
# HERO
# =============================================================================

st.markdown(
    """
<div class="home-hero">

<div class="home-eyebrow">
WELCOME TO
</div>

<div class="home-title">
Ella's Super Hot<br>
& Fantastic Blog
</div>

<div class="home-subtitle">
A SUPER special place on the internet, made with love and care, 
just for my beautiful girlfriend.
</div>

</div>
""",
    unsafe_allow_html=True,
)


# =============================================================================
# SITE INTRO
# =============================================================================

st.markdown(
    """
<div class="home-section-title">
DIFFERENT WEBSITE FEATURES
</div>
""",
    unsafe_allow_html=True,
)


# =============================================================================
# PAGE CARDS
# =============================================================================

southpark_col, twilight_col, blog_col = st.columns(3)


with southpark_col:

    st.markdown(
        """
<div class="home-card">
<div class="home-card-small">RANKINGS</div>
<div class="home-card-title">South Park</div>
<div class="home-card-description">
An extremely thourough ranking and rating of each South Park
episode, that was done with a lot of care and attention to detail.
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button(
        "View Episode Ranking →",
        key="southpark_home",
        use_container_width=True,
    ):
        st.switch_page("pages/southpark.py")


with twilight_col:

    st.markdown(
        """
<div class="home-card">
<div class="home-card-small">AUDIOBOOK</div>
<div class="home-card-title">Twilight #1</div>
<div class="home-card-description">
The super seriously read audiobook for Ella. 
Currently on the first book, but will eventually include all four books in the series.
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button(
        "Listen to my voice →",
        key="twilight_home",
        use_container_width=True,
    ):
        st.switch_page("pages/twilight.py")


with blog_col:

    st.markdown(
        """
<div class="home-card">
<div class="home-card-small">FROM MARIA'S BEAUTIFUL MIND</div>
<div class="home-card-title">The Blog Portion</div>
<div class="home-card-description">
Things that I think about, things that I do, and things that I want to share with you...
Which is basically everything that I do... 
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button(
        "Read →",
        key="blog_home",
        use_container_width=True,
    ):
        st.switch_page("pages/blog.py")


# =============================================================================
# FOOTER
# =============================================================================

st.markdown(
    """
<div class="home-footer" style="height: 1080px;"></div>
Made with a lot of love & coding for Ella <3 
</div>
""",
    unsafe_allow_html=True,
)