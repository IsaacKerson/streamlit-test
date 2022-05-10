import streamlit as st
import sqlite3

conn = sqlite3.connect('vocabulary.db')
c = conn.cursor()
unit = ("Unit 1",)

st.title("With SQLite")
for row in c.execute("SELECT * FROM vocab WHERE unit = ?", unit):
    st.write(row[2])

conn.close()