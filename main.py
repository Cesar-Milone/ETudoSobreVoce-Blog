from flask import Flask, render_template, jsonify
import json
from static.classes.bible_api import Bible
from datetime import datetime
from static.classes.db import Database

app = Flask(__name__)
bible = Bible()
#db = Database()
today = datetime.now().day

#db.post_title = "Titulo pelo Pycharm"
#db.post_subtitle = "Subtítulo pelo Pycharm"
#db.post_body = "Corpo do post"
#db.user_id = 1
#db.comment_id = 1
#db.exec_insert()


bible_num = 1
bible_text = ""


def change_bible_text():
    global today, bible_num, bible_text
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


with open("static/json_data.json", "r") as file:
    post_completed = json.load(file)

post_title = post_completed["0"]["post_title"]
post_subtitle = post_completed["0"]["post_subtitle"]
post_body = post_completed["0"]["post_body"]


@app.route("/")
def index():
    change_bible_text()
    return render_template("index.html", bible=bible_text, post_title=post_title,
                           post_subtitle=post_subtitle, post_body=post_body, post_completed=post_completed)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html", bible=bible, post_title=post_title,
                           post_subtitle=post_subtitle, post_body=post_body)


@app.route("/random")
def random_get():
    return jsonify(header="Esse e o titulo", post="Esse e o post completo")


if __name__ == "__main__":
    app.run(debug=True)
