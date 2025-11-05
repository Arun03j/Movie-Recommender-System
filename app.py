import streamlit as st
import pickle
import pandas as pd
import requests


movies_dict = pickle.load(open("/Users/aaron3j/Downloads/Projects/Movie Recommender System/movie_list.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("/Users/aaron3j/Downloads/Projects/Movie Recommender System/similarity.pkl", "rb"))


TMDB_API_KEY = "4bedff1bc4d82e2661349c95c032b67a" 


def fetch_poster(movie_name):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}"
        data = requests.get(url).json()
        if data['results']:
            poster_path = data['results'][0]['poster_path']
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path
        return "https://via.placeholder.com/500x750?text=No+Poster"
    except:
        return "https://via.placeholder.com/500x750?text=No+Poster"


def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    recommended_posters = []
    
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].title))
    
    return recommended_movies, recommended_posters


st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a Movie Name:", movies['title'].values)

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie)
    
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            poster_url = posters[idx]
            if not poster_url.startswith("http"):
                poster_url = "https://via.placeholder.com/500x750?text=No+Poster"
            st.image(poster_url)   
            st.caption(names[idx])

st.markdown(
    """
    <style>
    
    /* MAIN APP BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #141414, #000000);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a1a, #0d0d0d);
        color: white;
    }

    /* HEADER */
    [data-testid="stHeader"] {
        background: none;
    }

    /* TITLES */
    h1, h2, h3 {
        color: Blue; /* Netflix Red */
        text-shadow: 0px 0px 10px rgba(229, 9, 20, 0.8);
    }

    /* TEXT INPUT */
    .stTextInput > div > div > input {
        background-color: #1f1f1f;
        color: white;
        border: 1px solid #E50914;
        border-radius: 8px;
    }

    /* BUTTONS */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #E50914, #b0060f);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6em 1.5em;
        font-size: 1em;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px rgba(229, 9, 20, 0.5);
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 25px rgba(229, 9, 20, 0.8);
    }

    /* MOVIE CARD */
    .movie-card {
        background-color: #1a1a1a;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(229, 9, 20, 0.2);
        padding: 10px;
        text-align: center;
        transition: all 0.3s ease;
    }

    .movie-card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 35px rgba(229, 9, 20, 0.5);
    }

    .movie-title {
        color: #ffffff;
        margin-top: 10px;
        font-weight: 500;
    }

    /* WARNING/INFO MESSAGES */
    .stAlert {
        background-color: #1a1a1a !important;
        border-left: 5px solid #E50914 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)