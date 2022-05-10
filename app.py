import streamlit as st
import pymongo


cluster = "mongodb+srv://m001-student:test-run@sandbox.zqzg8.mongodb.net/sample_airbnb?retryWrites=true&w=majority"
client = pymongo.MongoClient(cluster, server_api=ServerApi('1'))
#db = client.test

st.title("With Pymongo")

#x = st.slider('Select a value')
#st.write(x, 'squared is', x * x)
st.write(client.list_database_names())