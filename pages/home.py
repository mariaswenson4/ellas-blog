import streamlit as st

from utils.styling.home import apply_home_styles


# =============================================================================
# PAGE STYLING
# =============================================================================

apply_home_styles()


# =============================================================================
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
Fantastic Blog
</div>

<div class="home-subtitle">
A highly unnecessary corner of the internet made by Maria,
for one very specific woman.
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
CHOOSE YOUR ADVENTURE
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
<div class="home-card-small">IMPORTANT RESEARCH</div>
<div class="home-card-title">South Park</div>
<div class="home-card-description">
An extremely serious and academically rigorous ranking
of every South Park episode.
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button(
        "View Rankings →",
        key="southpark_home",
        use_container_width=True,
    ):
        st.switch_page("pages/southpark.py")


with twilight_col:

    st.markdown(
        """
<div class="home-card">
<div class="home-card-small">NOW LISTENING</div>
<div class="home-card-title">Twilight</div>
<div class="home-card-description">
The critically acclaimed and completely unauthorized
Maria's Version audiobook experience.
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    if st.button(
        "Listen →",
        key="twilight_home",
        use_container_width=True,
    ):
        st.switch_page("pages/twilight.py")


with blog_col:

    st.markdown(
        """
<div class="home-card">
<div class="home-card-small">FROM THE DESK OF MARIA</div>
<div class="home-card-title">The Blog</div>
<div class="home-card-description">
Thoughts, observations, important announcements,
and other things you definitely needed to know.
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
<div class="home-footer">
Made with an unreasonable amount of Python for one specific woman. ♡
</div>
""",
    unsafe_allow_html=True,
)