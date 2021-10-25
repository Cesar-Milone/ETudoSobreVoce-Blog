from flask import Flask, render_template, jsonify, request
import json
from static.classes.bible_api import Bible
from datetime import datetime
from static.classes.db import Database
from random import randint
import logging
from static.classes.user import User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
bible = Bible()
db = Database()
today = datetime.now().day

bible_num = 1
bible_text = ""
user = User()


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
post_list_db = db.exec_select()
post_pandas = db.exec_select_pandas()
post_len = len(post_pandas) - 1


@app.route("/")
def index():
    change_bible_text()
    return render_template("index.html", user=user, bible=bible_text, post_list=post_pandas)


@app.route("/about")
def about():
    return render_template("about.html", user=user)


@app.route("/contact")
def contact():
    return render_template("contact.html", user=user)


@app.route("/login_page")
def login_page():
    return render_template("login.html", user=user)


@app.route("/register_page")
def register_page():
    return render_template("register.html", user=user)


@app.route("/login", methods=['POST'])
def login():
    global user
    data = request.form
    email = data["email"]
    password = data["password"]
    user = db.check_user(email)
    if check_password_hash(user.password_hash, password):
        user.validate = True
        if user.user_id == 1:
            user.admin = True
    return render_template("index.html", user=user, bible=bible_text, post_list=post_pandas)


@app.route("/register", methods=['POST'])
def register():
    global user
    data = request.form
    user.name = data["name"]
    user.email = data["email"]
    user.password_hash = generate_password_hash(
            data["password"],
            method='pbkdf2:sha256',
            salt_length=8
        )
    db.exec_insert_user(user)
    return render_template("index.html", user=user, bible=bible_text, post_list=post_pandas)


@app.route("/logoff")
def logoff():
    user.logoff()
    return render_template("index.html", user=user, bible=bible_text, post_list=post_pandas)


@app.route("/post<int:post_cod>")
def post(post_cod):
    post_title = post_pandas.post_title[post_cod]
    post_subtitle = post_pandas.post_subtitle[post_cod]
    post_body = post_pandas.post_body[post_cod]

    return render_template("post.html", user=user, bible=bible, post_title=post_title,
                           post_subtitle=post_subtitle, post_body=post_body)


@app.route("/new_post_page")
def new_post_page():
    return render_template("new_post.html", user=user, bible=bible)


@app.route("/new_post", methods=['POST'])
def new_post():
    global user, post_pandas
    data = request.form
    db.post_title = data["title"]
    db.post_subtitle = data["subtitle"]
    db.post_body = data["body"]
    db.exec_insert()
    post_pandas = db.exec_select_pandas()
    return render_template("index.html", user=user, bible=bible_text, post_list=post_pandas)


@app.route("/random")
def random_get():
    return render_template("post.html", user=user, bible=bible)


if __name__ == "__main__":
    app.run(debug=True)
