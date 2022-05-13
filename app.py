import streamlit as st
import sqlite3
import random
import datetime

# Custom imports
from multipage import MultiPage
from pages import quiz, upload

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.markdown("# Quiz Maker")

# Add all your application here
app.add_page("Quiz", quiz.app)
app.add_page("Upload", upload.app)
app.add_page("View", view.app)

# The main app
app.run()