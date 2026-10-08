
import streamlit as st


# =============================================================================
# REUSABLE HEADER STYLING
# =============================================================================

def apply_header_styles():
    """Apply shared page and section header styling."""

    st.markdown(
        """
        <style>

        /* =====================================================
           PAGE HEADERS
           ===================================================== */

        .site-page-header {
            text-align: center;
            margin: 20px auto 30px;
        }

        .site-header-eyebrow {
            font-size: 0.70rem;
            font-weight: 800;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-bottom: 12px;
            color: rgba(255, 255, 255, 0.65);
        }

        .site-header-title {
            font-family: Georgia, serif;
            font-size: 3.8rem;
            font-weight: 700;
            line-height: 1.1;
            margin-bottom: 18px;
            color: white;
        }

        .site-header-subtitle {
            max-width: 620px;
            margin: auto;
            font-family: Georgia, serif;
            font-size: 1rem;
            font-style: italic;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.75);
        }

        /* =====================================================
           SECTION HEADERS
           ===================================================== */

        .site-section-header {
            text-align: center;
            margin: 35px auto 20px;
        }

        .site-section-eyebrow {
            font-size: 0.65rem;
            font-weight: 800;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 8px;
            color: rgba(255, 255, 255, 0.60);
        }

        .site-section-title {
            font-family: Georgia, serif;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 8px;
            color: white;
        }

        .site-section-description {
            font-family: Georgia, serif;
            font-size: 0.95rem;
            font-style: italic;
            color: rgba(255, 255, 255, 0.70);
        }

        /* =====================================================
           HIDE EMPTY ELEMENTS
           ===================================================== */

        .site-header-eyebrow:empty,
        .site-header-subtitle:empty,
        .site-section-eyebrow:empty,
        .site-section-description:empty {
            display: none;
        }

        /* =====================================================
           MOBILE
           ===================================================== */

        @media (max-width: 800px) {
            .site-header-title {
                font-size: 2.7rem;
            }

            .site-section-title {
                font-size: 1.7rem;
            }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )
