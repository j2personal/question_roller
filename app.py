from flask import Flask, request, render_template
import os
import psycopg2

app = Flask(__name__)


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT question FROM questions")

        lst = cur.fetchall()
        print(lst)
        cur.close()
        return render_template("index.html")


    if request.method == 'POST':

        request.form.get("")







