import streamlit as st
import pymongo


uri = "mongodb+srv://m001-student:test-run@sandbox.zqzg8.mongodb.net"
client = pymongo.MongoClient(uri)
mflix = client.sample_mflix
movies = mflix.movies

st.title("With Pymongo")

#x = st.slider('Select a value')
#st.write(x, 'squared is', x * x)
st.write(movies.find_one())