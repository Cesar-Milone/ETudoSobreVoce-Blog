import json


def write_post_data(new_post):
    with open("static/json_data.json", "w") as file:
        json.dump(new_post, file)


class Post:
    def __init__(self):
        pass

    def post_add(self, post_title, post_subtitle, post_body):
        post_add = {
            "post_title": post_title,
            "post_subtitle": post_subtitle,
            "post_body": post_body,
        }
        post = self.read_post_data()
        post[len(post)] = post_add
        write_post_data(post)

    def read_post_data(self):
        with open("static/json_data.json", "r") as file:
            return json.load(file)
