import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open(r'C:\Users\Shambhavi\Documents\machine learning\movie recoomender\movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

option = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)
