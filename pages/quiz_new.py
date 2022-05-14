import streamlit as st
import os.path
import sqlite3
import random
import datetime
import re

# Custom imports
from pages.utils import add_blanks, chunker, random_session_id, check_answer, db_connect, chk_conn

def app():

    DATABASE_NAME = 'quiz_maker.db'
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE = os.path.join(BASE_DIR, DATABASE_NAME)

    def form_callback(questions):
        st.session_state.form_submit = True
        num_correct = 0
        session_id = random_session_id()
        student_id = 'UKWN'
        uct_iso = datetime.datetime.utcnow().isoformat()
        st.title("Feedback")
        for idx, items in enumerate(questions):
            answer = st.session_state[idx]
            correct_str = 'incorrect'
            correct_int = 0
            if check_answer(items[1], answer):
                correct_str = 'correct'
                correct_int = 1
                num_correct += 1
                st.success(f"Question {idx + 1}")
            else:
                st.error(f"Question {idx + 1}")
            st.write(f"{items[3]}")
            st.write(f"Answer: {items[1]}")
            st.write(f"Your answer: {answer}")
            st.write(f"You are {correct_str}.")
            insert_tup = (student_id, session_id, uct_iso, items[1], items[2], answer, correct_int, )
            c, conn = db_connect(DATABASE)
            c.execute("INSERT INTO responses VALUES (?, ?, ?, ?, ?, ?, ?)", insert_tup)
            conn.commit()
        conn.close()
        score_val = 100 * num_correct / len(questions)
        st.metric(label="Final Score", value=f"{score_val}%")
        
    if "form_submit" not in st.session_state:

        c, conn = db_connect(DATABASE)

        st.markdown("# Sentence Completion")
        st.text_input('Comma seperated tags. (Maximum 3)', key='tags')
        st.selectbox('How many question do you want?', [5,10,15,20], key='num_q')
        
        tag_string = st.session_state.tags
        num_q = st.session_state.num_q
        
        def clean_string(string):
            return re.sub('[^0-9a-zA-Z\s,]+', '', string)

        def split_string(string, split_on = ","):
            return [x.strip().upper() for x in string.split(split_on)]
        
        def make_subquery(terms, column = 'tags', operator = 'AND'):
            return f' {operator} '.join([f"{column} LIKE '%{x}%'" for x in terms if len(x) > 0])
        
        def make_query(subquery, limit = 10):
            return f"""SELECT * FROM vocab WHERE {subquery} ORDER BY RANDOM() LIMIT {str(limit)}"""

        clean_tags = clean_string(tag_string)
        terms = split_string(clean_tags)
        subquery = make_subquery(terms)
        query = make_query(subquery, limit = num_q)

        if tag_string:
            # for idx, item in enumerate(c.execute(query)):
            #     st.write(f'{idx}, {item}')

        st.markdown(f'## {terms}')
        st.write("Complete the sentences with the words from the word bank.")

        # questions = []
        # word_bank = []

        # query = "SELECT * FROM vocab WHERE unit = ? ORDER BY RANDOM() LIMIT ?"

        # for idx, item in enumerate(c.execute(query, input_tup)):
        #     word = item[2]
        #     word_bank.append(word)
        #     sentence = item[4]
        #     questions.append((idx, word, sentence, add_blanks(word, sentence)))

        # st.subheader("Word Bank")
        # random.shuffle(word_bank)
        # st.table(chunker(word_bank, 5))

        # with st.form("sentence_completion"):
        #     for q in questions:
        #         st.text_input(f'{q[0] + 1}. {q[3]}', key=q[0], placeholder="Type answer here")
        #     submitted = st.form_submit_button(label="Submit", on_click=form_callback, args=(questions,))
        #     if submitted:
        #         st.write("Submitted")
        # conn.close()
        