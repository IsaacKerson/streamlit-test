import streamlit as st
import os.path
import sqlite3

# Custom imports
from pages.utils import db_connect

def app():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE = os.path.join(BASE_DIR, 'vocabulary_current.db')

    c, conn = db_connect(DATABASE)

    query = st.text_input("Query", placeholder="Type answer here") 