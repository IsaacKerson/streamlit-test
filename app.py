import streamlit as st
import sqlite3



conn = sqlite3.connect('vocabulary.db')
c = conn.cursor()
unit = "Unit 1"
unit_tup = (unit,)

st.title(unit)

units_list = []
for item in c.execute("SELECT DISTINCT unit FROM vocab"):
  units_list.append(item[0])
st.write(units_list)

# for row in c.execute("SELECT * FROM vocab WHERE unit = ?", unit_tup):
#     st.write(row[2])

conn.close()