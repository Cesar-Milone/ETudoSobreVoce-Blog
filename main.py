from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/random")
def random_get():
    return jsonify(header="Esse e o titulo", post="Esse e o post completo")


if __name__ == "__main__":
    app.run(debug=True)
