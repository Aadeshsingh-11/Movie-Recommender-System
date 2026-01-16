import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list:
        print(new_df.iloc[i[0]].title)
from main import recommend

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies= pd.DataFrame(movies_dict)
st.title('Movie Recommendation System')


selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values,
)

if st.button("Recommend"):
    recommend(selected_movie_name)
    st.write("selected_movie_name")