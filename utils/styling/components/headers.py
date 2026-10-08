
import html
import textwrap

import streamlit as st


# =============================================================================
# REUSABLE PAGE HEADER
# =============================================================================

def render_page_header(
    title: str,
    subtitle: str = "",
    eyebrow: str = "",
    theme: str = "default",
):
    """Render a reusable page header."""

    title = html.escape(title)
    subtitle = html.escape(subtitle)
    eyebrow = html.escape(eyebrow)
    theme = html.escape(theme, quote=True)

    st.markdown(
        textwrap.dedent(
            f"""
            <div class="site-page-header theme-{theme}">
                <div class="site-header-eyebrow">{eyebrow}</div>
                <div class="site-header-title">{title}</div>
                <div class="site-header-subtitle">{subtitle}</div>
            </div>
            """
        ).strip(),
        unsafe_allow_html=True,
    )


# =============================================================================
# REUSABLE SECTION HEADER
# =============================================================================

def render_section_header(
    title: str,
    description: str = "",
    eyebrow: str = "",
    theme: str = "default",
):
    """Render a reusable section header."""

    title = html.escape(title)
    description = html.escape(description)
    eyebrow = html.escape(eyebrow)
    theme = html.escape(theme, quote=True)

    st.markdown(
        textwrap.dedent(
            f"""
            <div class="site-section-header theme-{theme}">
                <div class="site-section-eyebrow">{eyebrow}</div>
                <div class="site-section-title">{title}</div>
                <div class="site-section-description">{description}</div>
            </div>
            """
        ).strip(),
        unsafe_allow_html=True,
    )
