import streamlit as st
import sqlite3

conn = sqlite3.connect('vocabulary.db')
cursor = conn.cursor
unit = ("Unit 1",)
cursor.execute("SELECT * FROM vocab WHERE unit = ?", unit)
st.title("With SQLite")
st.write(cursor.fetchone())