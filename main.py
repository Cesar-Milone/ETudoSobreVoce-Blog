from flask import Flask, render_template, jsonify
import json
from bible_api import Bible

app = Flask(__name__)
bible = Bible()

with open("static/json_data.json", "r") as file:
    post_completed = json.load(file)

post_title = post_completed["0"]["post_title"]
post_subtitle = post_completed["0"]["post_subtitle"]
post_body = post_completed["0"]["post_body"]


@app.route("/")
def index():
    return render_template("index.html", bible=bible.text1, post_title=post_title,
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
