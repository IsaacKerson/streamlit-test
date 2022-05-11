import streamlit as st
import sqlite3



conn = sqlite3.connect('vocabulary.db')
c = conn.cursor()

units_list = []
for item in c.execute("SELECT DISTINCT unit FROM vocab"):
  units_list.append(item[0])

st.selectbox('Select a unit.', units_list, key='unit')
st.selectbox('How many question do you want?', [5,10,15,20], key='num_q')
unit = st.session_state.unit
num_q = st.session_state.num_q
input_tup = (unit, num_q)

st.title(unit)

for row in c.execute("SELECT * FROM vocab WHERE unit = ? LIMIT ?", input_tup):
    st.write(row[2])

conn.close()