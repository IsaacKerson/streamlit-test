import re
import random
import datetime
import os.path
import string
import sqlite3
import re

def add_blanks(word, sentence, blank = "__"):
  return re.sub(word, blank, sentence, flags=re.IGNORECASE)

def chunker(seq, size):
  return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def random_session_id():
  alphabet = string.ascii_lowercase + string.digits
  return ''.join(random.choices(alphabet, k=12))

def check_answer(item, answer):
  return item == answer

def clean_string(string):
  return re.sub('[^0-9a-zA-Z\s,]+', '', string)

def split_string(string, split_on = ","):
  return [x.strip().upper() for x in string.split(split_on)]

def make_subquery(terms, column = 'tags', operator = 'AND'):
  return f' {operator} '.join([f"{column} LIKE '%{x}%'" for x in terms if len(x) > 0])

def make_query(subquery, limit = 10):
  return f"""SELECT * FROM vocab WHERE {subquery} ORDER BY RANDOM() LIMIT {str(limit)}"""

def db_path(database):
    dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir, database)

def db_connect(database):
  conn = sqlite3.connect(database)
  c = conn.cursor()
  return c, conn

def chk_conn(conn):
  try:
    conn.cursor()
    return True
  except Exception as ex:
    return False

def get_tables(cursor):      
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  return cursor.fetchall()