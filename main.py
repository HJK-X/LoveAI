from flask import Flask, render_template
from flask import request

import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
from predict import predict

import random

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

predictions = []
starts = []
tokenizer = None
model = None
loaded = False
name, pronoun, likes, dislikes = "", "", [""], [""]


@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')


@app.route("/step1", methods=["GET"])
def step1():
    return render_template('step1.html')


@app.route("/step2", methods=["GET"])
def step2():
    return render_template('step2.html')


@app.route("/refresh", methods=["GET"])
def refresh():
    return getPrediction()


@app.route("/load", methods=["POST"])
def loadModel():
    global tokenizer, model, loaded
    tokenizer = AutoTokenizer.from_pretrained("HJK/PickupLineGenerator")
    model = AutoModelForCausalLM.from_pretrained("HJK/PickupLineGenerator")

    sepData()
    getStarts()
    addPreds()

    loaded = True


def sepData():
    global name, pronoun, likes, dislikes
    if request.form:
        data = request.form
    else:
        return
    name = data["name"]
    pronoun = data["pronoun"]
    likes = data["likes"].split(", ")
    dislikes = data["dislikes"].split(", ")


def getStarts():
    global starts
    for like in likes:
        starts.append("I like you like a "+like)
        starts.append("Are you a "+like)
    for dislike in dislikes:
        starts.append("I know you hate "+dislike)

    starts.append("Hi "+name+", ")
    starts.append("")

    starts.append("I")
    starts.append("You")

    random.shuffle(starts)


def getPrediction():
    if len(predictions) == 0:
        if not loaded:
            loadModel()
        addPreds()

    return nextPred()


def addPreds():
    rng = random.randint(0, len(starts)-1)
    predictions.extend(predict(starts[rng], model, tokenizer))
    random.shuffle(predictions)


def nextPred():
    global predictions
    pred = predictions[0]
    predictions.pop(0)
    print(pred)
    return pred


if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)
