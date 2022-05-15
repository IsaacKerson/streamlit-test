import streamlit as st
import os.path
import sqlite3

# Custom imports
from pages.utils import db_connect

def app():
    
    '''delete form_submit to run quiz maker on return to page'''
    if "form_submit" in st.session_state.keys():
        del st.session_state.form_submit
    if "form_upload" in st.session_state.keys():
        del st.session_state.form_upload
    
    st.markdown("## View Data")

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE = os.path.join(BASE_DIR, 'quiz_maker.db')

    c, conn = db_connect(DATABASE)

    size_query = "SELECT page_count * page_size as size FROM pragma_page_count(), pragma_page_size()"
    
    c.execute(size_query)
    
    st.markdown(f'##### Database size: {int(c.fetchone()[0] / 1000)} KB')

    query = st.text_input("Query", placeholder="Type query here")

    if len(query) > 1:
        try:
            for idx, item in enumerate(c.execute(query)):
                st.write(f'{idx}: {item}')
        except Exception as e:
            st.write("Query failed: " + str(e).capitalize())
