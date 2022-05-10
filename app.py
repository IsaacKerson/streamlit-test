import streamlit as st
import pymongo

uri = "mongodb+srv://m220student:test@sandbox.zqzg8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri, connect=False)
mflix = client.sample_mflix

movies = mflix.movies

st.title("With Pymongo")
st.write(movies.find_one())