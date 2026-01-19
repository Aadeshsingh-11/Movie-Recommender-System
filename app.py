import streamlit as st
import pickle
import pandas as pd
from main import recommend   

# load movie data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)

    for movie in recommendations:
        st.write("👉", movie)
