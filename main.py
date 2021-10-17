from flask import Flask, render_template, jsonify
import json
from static.classes.bible_api import Bible
from datetime import datetime
from static.classes.db import Database
from random import randint
import pandas as pd
import logging

logging.info("Startin application")
print("Startin application")

app = Flask(__name__)
bible = Bible()
db = Database()
today = datetime.now().day

bible_num = 1
bible_text = ""


def change_bible_text():
    global today, bible_num, bible_text
    logging.info("bible webscrapping")
    new_day = datetime.now().day
    if today != new_day:
        bible.get_versivulo()
        today = new_day
    if bible_num == 1:
        bible_num = 2
        bible_text = bible.text1
    elif bible_num == 2:
        bible_num = 1
        bible_text = bible.text2

logging.info("Open json")
with open("static/json_data.json", "r") as file:
    logging.info("Json opened")
    post_list = json.load(file)

# Start values to test de DB in server
for post in post_list:
    logging.info("Starting DB configuration")
    db.post_title = post_list[post]["post_title"]
    db.post_subtitle = post_list[post]["post_subtitle"]
    db.post_body = post_list[post]["post_body"]
    db.user_id = 1
    db.comment_id = 1
    db.exec_insert()
logging.info("Finish DB configuration")
post_list_db = db.exec_select()
post_pandas = db.exec_select_pandas()
logging.info("First entering in index.html")


@app.route("/")
def index():
    change_bible_text()
    return render_template("index.html", bible=bible_text, post_list=post_pandas)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post<int:post_cod>")
def post(post_cod):
    post_title = post_pandas.post_title[post_cod]
    post_subtitle = post_pandas.post_subtitle[post_cod]
    post_body = post_pandas.post_body[post_cod]

    return render_template("post.html", bible=bible, post_title=post_title,
                           post_subtitle=post_subtitle, post_body=post_body)


@app.route("/random")
def random_get():
    post_len = len(post_pandas) - 1
    post_cod = randint(0, post_len)
    post_title = post_pandas.post_title[post_cod]
    post_subtitle = post_pandas.post_subtitle[post_cod]
    post_body = post_pandas.post_body[post_cod]

    return render_template("post.html", bible=bible, post_title=post_title,
                           post_subtitle=post_subtitle, post_body=post_body)


if __name__ == "__main__":
    app.run(debug=True)
