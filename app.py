import streamlit as st
import sqlite3

conn = sqlite3.connect('vocabulary.db')
c = conn.cursor()
unit = ("Unit 1",)
c.execute("SELECT * FROM vocab WHERE unit = ?", unit)
st.title("With SQLite")
st.write(c.fetchone()))