
import html
import random
from urllib.parse import urljoin, urlparse
import feedparser
import requests
import streamlit as st
from bs4 import BeautifulSoup
from utils.styling.movies import apply_movies_styles
from utils.styling.backgroundhelper import render_background
from utils.styling.headers import apply_header_styles
from utils.styling.components.headers import (
    render_page_header,
    render_section_header,
)
from utils.styling.components.html import render_html


# =============================================================================
# PAGE STYLING
# =============================================================================

apply_header_styles()
apply_movies_styles()
render_background(
    image_name="moviesbackground.png",
    overlay=0.12,
)
st.markdown(
    """
    <link
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded&display=block"
        rel="stylesheet"
    >
    """,
    unsafe_allow_html=True,
)
# =============================================================================
# LETTERBOXD SETTINGS
# =============================================================================

LETTERBOXD_USERNAME = "mariaswenson"
LETTERBOXD_RSS = (
    f"https://letterboxd.com/{LETTERBOXD_USERNAME}/rss/"
)

LETTERBOXD_WATCHLIST = (
    f"https://letterboxd.com/{LETTERBOXD_USERNAME}/watchlist/"
)

REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0",
}


# =============================================================================
# HELPERS
# =============================================================================

def safe_text(value):
    """Escape text before inserting it into HTML."""
    return html.escape(str(value or ""))


def safe_url(value):
    """Allow only HTTP and HTTPS links in generated HTML."""

    if not value:
        return ""

    value = str(value).strip()
    parsed = urlparse(value)

    if parsed.scheme not in ("http", "https"):
        return ""

    return html.escape(value, quote=True)


def split_movie_title(full_title):
    """Separate a movie title from its release year."""

    full_title = str(full_title or "")

    if full_title.endswith(")") and "(" in full_title:
        title, year = full_title.rsplit("(", 1)
        year = year.rstrip(")").strip()

        if year.isdigit() and len(year) == 4:
            return title.strip(), year

    return full_title, ""


def format_rating(rating):
    """Convert a Letterboxd rating into stars."""

    if rating in ("", None):
        return "Not Yet Rated"

    try:
        value = float(rating)
        full_stars = int(value)
        half_star = value - full_stars >= 0.5

        stars = "★" * full_stars

        if half_star:
            stars += "½"

        return stars or "Not rated"

    except (ValueError, TypeError):
        return str(rating)


def parse_letterboxd_description(description):
    """Extract a movie poster and text from an RSS description."""

    soup = BeautifulSoup(
        description or "",
        "html.parser",
    )

    image = soup.find("img")
    poster_url = image.get("src") if image else None

    if image:
        image.decompose()

    description_text = soup.get_text(
        " ",
        strip=True,
    )

    return poster_url, description_text


def render_movie_poster(poster_url, link, title):
    """Display a clickable movie poster."""

    poster = safe_url(poster_url)
    movie_link = safe_url(link)
    movie_title = safe_text(title)

    if not poster:
        st.caption("Poster unavailable")
        return

    if movie_link:
        render_html(
            f"""
            <a href="{movie_link}"
               target="_blank"
               rel="noopener noreferrer"
               class="movie-poster-link">
                <img src="{poster}"
                     class="clickable-movie-poster"
                     alt="{movie_title}">
            </a>
            """
        )
    else:
        st.image(
            poster_url,
            use_container_width=True,
        )


def render_movie_details(
    title,
    year="",
    rating=None,
    watched_date=None,
    rewatch=False,
    watchlist=False,
):
    """Display movie information using the existing CSS classes."""

    title_class = (
        "watchlist-title"
        if watchlist
        else "recent-movie-title"
    )

    year_class = (
        "watchlist-year"
        if watchlist
        else "recent-movie-year"
    )

    render_html(
        f"""
        <div class="{title_class}">
            {safe_text(title)}
        </div>
        """
    )

    if year:
        render_html(
            f"""
            <div class="{year_class}">
                {safe_text(year)}
            </div>
            """
        )

    if rating is not None:
        render_html(
            f"""
            <div class="movie-rating">
                {safe_text(format_rating(rating))}
            </div>
            """
        )

    if watched_date:
        render_html(
            f"""
            <div class="movie-date">
                Watched {safe_text(watched_date)}
            </div>
            """
        )

    if rewatch:
        st.caption("↻ Rewatch")


# =============================================================================
# LETTERBOXD DATA
# =============================================================================

@st.cache_data(ttl=600)
def load_letterboxd():
    """Load recent movies from Letterboxd RSS."""

    return feedparser.parse(LETTERBOXD_RSS)


@st.cache_data(ttl=600)
def load_watchlist():
    """Load the Letterboxd watchlist page."""

    response = requests.get(
        LETTERBOXD_WATCHLIST,
        headers=REQUEST_HEADERS,
        timeout=10,
    )

    response.raise_for_status()

    return BeautifulSoup(
        response.text,
        "html.parser",
    )


@st.cache_data(ttl=3600)
def get_movie_poster(movie_link):
    """Find a movie poster using Letterboxd's Open Graph image."""

    if not movie_link:
        return None

    try:
        response = requests.get(
            movie_link,
            headers=REQUEST_HEADERS,
            timeout=10,
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        poster_meta = soup.find(
            "meta",
            property="og:image",
        )

        if poster_meta:
            return poster_meta.get("content")

    except requests.RequestException:
        return None

    return None


def get_watchlist_movies():
    """Extract movie titles, links, and posters from the watchlist."""

    soup = load_watchlist()
    movies = []

    movie_components = soup.find_all(
        "div",
        attrs={
            "data-component-class": "LazyPoster",
        },
    )

    for component in movie_components:

        title = component.get(
            "data-item-full-display-name",
            "",
        )

        target_link = component.get(
            "data-target-link",
            "",
        )

        if not title:
            continue

        movie_link = (
            urljoin("https://letterboxd.com", target_link)
            if target_link
            else None
        )

        poster_url = get_movie_poster(movie_link)

        movies.append(
            {
                "title": title,
                "poster": poster_url,
                "link": movie_link,
            }
        )

    return movies


# =============================================================================
# PAGE HEADER
# =============================================================================

render_page_header(
    title="Maria in the Cinema",
    eyebrow="A LOOK INTO MY LIMITED FILM EXPERIENCE",
    subtitle=(
        "A almost comprehensive list of the movies I've watched, along with some of my silly opinions"
    ),
    theme="movies",
)


# =============================================================================
# RECENTLY WATCHED
# =============================================================================

render_section_header(
    title="Most Recently Watched",
    eyebrow="THE NEWEST",
    description="The most recent movies that I have seen, or that we have seen together. Ommiting movies that we did not ACTUALLY watch.",
    theme="movies",
)

feed = load_letterboxd()

if not feed.entries:
    st.error("I couldn't find any Letterboxd activity.")
    st.write("Feed:", LETTERBOXD_RSS)

else:

    recent_entries = feed.entries[:8]
    columns = st.columns(4)

    for index, entry in enumerate(recent_entries):

        title = entry.get(
            "letterboxd_filmtitle",
            entry.get("title", "Unknown Movie"),
        )

        year = entry.get("letterboxd_filmyear", "")
        rating = entry.get("letterboxd_memberrating", "")
        watched_date = entry.get("letterboxd_watcheddate", "")
        rewatch = entry.get("letterboxd_rewatch", "No")
        link = entry.get("link", "")
        description = entry.get("description", "")

        poster_url, _ = parse_letterboxd_description(
            description
        )

        with columns[index % 4]:

            render_movie_poster(
                poster_url=poster_url,
                link=link,
                title=title,
            )

            render_movie_details(
                title=title,
                year=year,
                rating=rating,
                watched_date=watched_date,
                rewatch=str(rewatch).lower() == "yes",
            )


# =============================================================================
# WATCHLIST
# =============================================================================

st.markdown("---")

render_section_header(
    title="Our Next Movie",
    eyebrow="UP NEXT... ",
    description="Movies that we have added  to my Letterboxd watchlist!",
    theme="movies",
)

watchlist_movies = []

try:
    watchlist_movies = get_watchlist_movies()

except requests.RequestException as error:
    st.error(f"Could not load watchlist: {error}")


# =============================================================================
# WATCHLIST PREVIEW
# =============================================================================

if watchlist_movies:

    preview_movies = watchlist_movies[:4]
    watchlist_columns = st.columns(4)

    for index, movie in enumerate(preview_movies):

        display_title, display_year = split_movie_title(
            movie["title"]
        )

        with watchlist_columns[index]:

            render_movie_poster(
                poster_url=movie["poster"],
                link=movie["link"],
                title=display_title,
            )

            render_movie_details(
                title=display_title,
                year=display_year,
                watchlist=True,
            )

else:
    st.info("No watchlist movies are available right now.")


# =============================================================================
# FULL WATCHLIST BUTTON
# =============================================================================

st.write("")

left, center, right = st.columns([1, 2, 1])

with center:
    st.link_button(
        ":material/movie: CLICK FOR FULL WATCHLIST!",
        LETTERBOXD_WATCHLIST,
        use_container_width=True,
    )




# =============================================================================
# RANDOM MOVIE PICKER
# =============================================================================

if "movie_pick" not in st.session_state:
    st.session_state.movie_pick = None


# =============================================================================
# SIDE-BY-SIDE RANDOMIZER
# =============================================================================

left_col, right_col = st.columns(
    [1, 1],
    gap="large",
    vertical_alignment="center",
)



# =============================================================================
# LEFT: RANDOMIZER CONTROLS
# =============================================================================

with left_col:

    with st.container(key="randomizer_left"):

        render_html(
            """
            <div class="randomizer-intro">
                <div class="randomizer-eyebrow">
                    A RANDOMIZED MOVIE PICKER
                </div>

                <div class="randomizer-title">
                    Shuffle Movies!
                </div>

                <div class="randomizer-description">
                    Let a random algorithm decide what movie from our watchlist that we should watch!
                </div>
            </div>
            """
        )

        if watchlist_movies:

            if st.session_state.movie_pick is None:
                button_label = ":material/shuffle: Pick Something for Us"
            else:
                button_label = ":material/casino: Reroll!"

            if st.button(
                button_label,
                key="random_movie_button",
                use_container_width=True,
            ):
                st.session_state.movie_pick = random.choice(
                    watchlist_movies
                )
                st.rerun()

        else:
            st.caption("The watchlist DNE.")

# =============================================================================
# RIGHT: MOVIE SELECTION
# =============================================================================

with right_col:

    with st.container(key="randomizer_right"):

        if st.session_state.movie_pick is None:

            render_html(
                """
                <div class="random-movie-placeholder">
                    <div class="random-placeholder-icon">
                        <span class="material-symbols-rounded">movie</span>
                    </div>
                    <div class="random-placeholder-title">
                        No Movie Picked Yet
                    </div>
                    <div class="random-placeholder-description">
                        Click the shuffle button to see what movie we're watching today!
                    </div>
                </div>
                """
            )

        else:

            movie = st.session_state.movie_pick

            render_html(
                f"""
                <div class="random-movie-result">
                    <div class="random-result-eyebrow">
                        Let's Watch...
                    </div>
                    <div class="random-result-title">
                        {safe_text(movie["title"])}
                    </div>
                </div>
                """
            )

            if movie["poster"]:

                poster_left, poster_center, poster_right = st.columns(
                    [1, 3, 1]
                )

                with poster_center:
                    st.image(
                        movie["poster"],
                        use_container_width=True,
                    )

            if movie["link"]:
                st.link_button(
                    ":material/link: View on Letterboxd →",
                    movie["link"],
                    use_container_width=True,
                )


