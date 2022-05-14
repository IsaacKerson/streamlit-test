import streamlit as st
import os.path
import sqlite3

# Custom imports
from pages.utils import db_connect

def app():
    
    '''delete form_submit to run quiz maker on return to page'''
    del st.session_state.form_submit
    
    st.markdown("## View Data")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE = os.path.join(BASE_DIR, 'quiz_maker.db')

    c, conn = db_connect(DATABASE)

    query = st.text_input("Query", placeholder="Type query here")

    if len(query) > 1:
        try:
            for idx, item in enumerate(c.execute(query)):
                st.write(f'{idx}: {item}')
        except Exception as error:
            st.write(error)
