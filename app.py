import streamlit as st
import pymongo

server_api = pymongo.server_api.ServerApi('1')
uri = "mongodb+srv://m001-student:test@sandbox.zqzg8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri, server_api=server_api)
mflix = client.sample_mflix
movies = mflix.movies

st.title("With Pymongo")
st.write(movies.find_one())