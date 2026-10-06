import streamlit as st


# =============================================================================
# HEADER
# =============================================================================

st.markdown(
    """
<div style="text-align: center; margin-bottom: 35px;">

<h1>Maria's Movie Archive</h1>

<p>
Because I have literally never seen a single damn thing like ever, and I need to keep track and give you ample review lol
</p>

</div>
""",
    unsafe_allow_html=True,
)


# =============================================================================
# LETTERBOXD
# =============================================================================

st.markdown(
    """
<div style="
    max-width: 700px;
    margin: auto;
    text-align: center;
    padding: 35px;
    border-radius: 18px;
    background: rgba(20, 20, 20, 0.85);
">

<h2>@mariaswenson</h2>

<p>
</p>

</div>
""",
    unsafe_allow_html=True,
)


st.link_button(
    "Open My Personal Letterboxd Here→",
    "https://letterboxd.com/mariaswenson/",
    use_container_width=True,
)