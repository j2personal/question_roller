from flask import Flask, request, render_template, redirect, url_for
import os
import psycopg2
import random

app = Flask(__name__)


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


    if request.method == 'POST':
        cur = conn.cursor()
        cur.execute("SELECT question FROM questions")
        lst = cur.fetchall()
        cur.close()

        item = random.choice(lst)[0]

        return(item)

@app.route('/view', methods=['GET'])
def view():
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM questions")
        lst = [(item[0], item[1]) for item in cur.fetchall()]
        print(lst)

        cur.close()
        return render_template("view.html", lst=lst)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        new_q = request.form.get("new_q")
        cur = conn.cursor()
        
        cur.execute(f"INSERT INTO questions (question) VALUES (\'{new_q}\')")
        lst = cur.fetchall()
        cur.close()

        return(item)

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        row_id = request.form.get("row_id")
        cur = conn.cursor()
        
        cur.execute(f"DELETE FROM questions WHERE question_id = {row_id}")
        lst = cur.fetchall()
        cur.close()

        return redirect(url_for('view'))










