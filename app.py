from flask import Flask, request, render_template
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
        print(lst)
        cur.close()

        item = random.choice(lst)[0]

        return(item)







