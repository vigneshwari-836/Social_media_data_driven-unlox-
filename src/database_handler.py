import sqlite3
import pandas as pd
def initialize_database():
   
    conn = sqlite3.connect('social_initiative.db')
    cursor = conn.cursor()
    # Create a table for our social media posts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        date TEXT,
        topic TEXT,
        likes INTEGER,
        shares INTEGER,
        saves INTEGER,
        comments TEXT
        )
    ''')
    conn.commit()
    conn.close()
def save_to_db(df):

    conn = sqlite3.connect('social_initiative.db')
    df.to_sql('posts', conn, if_exists='replace', index=False)
    conn.close()
