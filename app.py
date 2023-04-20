import streamlit as st
import pickle

st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)