import textwrap
import streamlit as st


def render_html(content: str):
    """Render HTML without Markdown displaying it as code."""

    cleaned = textwrap.dedent(content).strip()

    cleaned = "\n".join(
        line.lstrip()
        for line in cleaned.splitlines()
    )

    st.markdown(
        cleaned,
        unsafe_allow_html=True,
    )