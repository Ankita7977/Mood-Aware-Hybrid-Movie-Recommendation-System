import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
img { border-radius: 14px; }
.movie-card { padding: 10px; }
</style>
""", unsafe_allow_html=True)

# ---------------- MOOD → GENRE MAP ----------------
MOOD_GENRES = {
    "Happy 😊": ["Comedy", "Adventure", "Animation", "Family"],
    "Sad 😢": ["Drama", "Romance"],
    "Romantic ❤️": ["Romance", "Drama"],
    "Excited 🤩": ["Action", "Adventure", "Sci-Fi", "Thriller"],
    "Scary 😱": ["Horror", "Thriller", "Mystery"],
    "Relax 😌": ["Fantasy", "Family", "Animation", "Music"],
    "Dark 🖤": ["Crime", "Drama", "Thriller", "Mystery"]
}

# ---------------- TMDB CONFIG ----------------
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
POSTER_URL = "https://image.tmdb.org/t/p/w500"

# ---------------- FETCH MOVIE DETAILS ----------------
@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        poster = (
            POSTER_URL + data["poster_path"]
            if data.get("poster_path")
            else "https://via.placeholder.com/500x750?text=No+Image"
        )

        return {
            "poster": poster,
            "rating": data.get("vote_average", "N/A"),
            "year": data.get("release_date", "")[:4],
            "genres": ", ".join([g["name"] for g in data.get("genres", [])]),
            "overview": data.get("overview", "No description available")
        }

    except:
        return None

# ---------------- LOAD DATA ----------------
movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# ----------- CREATE SIMILARITY RUNTIME -----------
@st.cache_data
def create_similarity(dataframe):
    cv = CountVectorizer(max_features=5000, stop_words="english")
    vectors = cv.fit_transform(dataframe["tags"]).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

similarity = create_similarity(movies)

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie_title, mood):
    if movie_title not in movies["title"].values:
        return []

    movie_index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[movie_index]

    similar_movies = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:60]

    mood_genres = MOOD_GENRES[mood]
    recommendations = []

    for idx, _ in similar_movies:
        movie_row = movies.iloc[idx]

        if any(
            genre.lower() in str(movie_row["tags"]).lower()
            for genre in mood_genres
        ):
            details = fetch_movie_details(movie_row.movie_id)

            if details:
                recommendations.append({
                    "title": movie_row.title,
                    **details
                })

        if len(recommendations) == 5:
            break

    return recommendations

# ---------------- UI ----------------
st.title("🎬 Mood-Aware Hybrid Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie you like",
    movies["title"].values
)

selected_mood = st.selectbox(
    "Select your mood",
    list(MOOD_GENRES.keys())
)

if st.button("Recommend 🎥"):
    with st.spinner("Finding movies for you..."):
        results = recommend(selected_movie, selected_mood)

    if results:
        st.markdown(
            f"### Because you liked {selected_movie} and feel {selected_mood}"
        )

        cols = st.columns(5)

        for i, movie in enumerate(results):
            with cols[i]:
                st.image(movie["poster"], use_container_width=True)
                st.markdown(f"### {movie['title']}")
                st.markdown(f"⭐ {movie['rating']} | 📅 {movie['year']}")
                st.markdown(f"Genres: {movie['genres']}")

                with st.expander("👁 View details"):
                    st.write(movie["overview"])
    else:
        st.warning("No recommendations found for this mood.")
