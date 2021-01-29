from flask import Flask, render_template
from flask import request

import torch
import transformers
from predict import predict


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/", methods=["GET"]) 
def main():
    return render_template('index.html')


@app.route("/step1", methods=["GET"])
def step1():
    return render_template('step1.html')


@app.route("/step2", methods=["GET", "POST"])
def step2():
    if request.method == "POST":
        loadModel()
    return render_template('step2.html')


def sepData():
    data = request.form
    name = data["name"]
    pronoun = data["pronoun"]
    likes = data["likes"].split(", ")
    dislikes = data["dislikes"].split(", ")

    return name, pronoun, likes, dislikes

def loadModel():
    




if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
 