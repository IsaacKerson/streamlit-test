import streamlit as st
import sqlite3
import random
import datetime

# Custom imports
from multipage import MultiPage
from pages import quiz, upload
# from pages.utils import add_blanks, chunker, random_session_id, check_answer

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.markdown("# Quiz Maker")

# Add all your application here
app.add_page("Quiz", quiz.app)
app.add_page("Upload", upload.app)

# The main app
app.run()