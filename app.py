import streamlit as st
import pymongo

uri = "mongodb+srv://m220student:test@sandbox.zqzg8.mongodb.net/sample_mflix/movies?ssl=true&ssl_cert_reqs=CERT_NONE"
client = pymongo.MongoClient(uri)
mflix = client.sample_mflix

movies = mflix.movies

st.title("With Pymongo")
st.write(movies.find_one())