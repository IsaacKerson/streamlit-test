import re
import random
import datetime
import string
import sqlite3

def add_blanks(word, sentence, blank = "__"):
  return re.sub(word, blank, sentence, flags=re.IGNORECASE)

def chunker(seq, size):
  return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def random_session_id():
  alphabet = string.ascii_lowercase + string.digits
  return ''.join(random.choices(alphabet, k=12))

def check_answer(item, answer):
  return item == answer

def chk_conn(conn):
  try:
    conn.cursor()
    return True
  except Exception as ex:
    return False

def get_tables(cursor):      
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  return cursor.fetchall()