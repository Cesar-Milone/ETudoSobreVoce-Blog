from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
dictionary = {
    "post_title": "Pessoas Motivadas / Desmotivadas",
    "post_subtitle": "Lembre-se que Deus é o seu consolo, em meio a tanto problemas, por mais difícil que esteja.",
    "post_body": "Esse é o corpo de descrição de todo o texto.",
}
#with open("static/json_data.json", "w") as file:
#    json.dump(dictionary, file)
with open("static/json_data.json", "r") as file:
    post_completed = json.load(file)

bible = "Também no caminho dos teus juízos, Senhor, te esperamos;" \
        " no teu nome e na tua memória está o desejo da nossa alma. Isaías 26:8"
post_title = post_completed["post_title"]
post_subtitle = post_completed["post_subtitle"]
post_body = post_completed["post_body"]


@app.route("/")
def index():
    return render_template("index.html", bible=bible, post_title=post_title,
                           post_subtitle=post_subtitle, post_body=post_body)


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
