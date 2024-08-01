from flask import Flask, render_template, request
import random
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS used_letters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        letter TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

create_tables()

WORD_LIST = ["ELMA", "PORTAKAL", "ARMUT"]
word = random.choice(WORD_LIST)
used_letters = set()
TRIES = 6
IMG = 0

@app.before_request
def initialize_game():
    global used_letters, word, TRIES, IMG
    if request.endpoint == 'game' and request.method == 'GET':
        used_letters = set()
        TRIES = 6
        IMG = 0
        word = random.choice(WORD_LIST)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM used_letters')
        conn.commit()
        conn.close()

@app.route("/", methods=["GET", "POST"])
def game():
    global used_letters, TRIES, word, IMG

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        letter = request.form.get("letter")
        if letter:
            cursor.execute('INSERT INTO used_letters (letter) VALUES (?)', (letter))
            conn.commit()
            if letter not in word:
                TRIES -= 1
                IMG += 1
            if TRIES == 0:
                conn.close()
                return render_template("gameover.html")

    cursor.execute('SELECT letter FROM used_letters')
    used_letters = set(row['letter'] for row in cursor.fetchall())

    word_list = [letter if letter in used_letters else "_" for letter in word]
    current_word = " ".join(word_list)

    if "_" not in word_list:
        conn.close()
        return render_template("win.html", word=word)

    conn.close()
    return render_template("index.html", current_word=current_word, tries=TRIES, img=IMG)
