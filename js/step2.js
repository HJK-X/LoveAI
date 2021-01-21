import * as tf from '@tensorflow/tfjs';
import {loadGraphModel} from '@tensorflow/tfjs-converter';

const MODEL_URL = 'model_directory/model.json';

const model = await loadGraphModel(MODEL_URL);

function generate() {
    var name = localStorage.getItem("name");
    var pronoun = localStorage.getItem("pronoun");
    var likes = localStorage.getItem("likes");
    var dislikes = localStorage.getItem("dislikes")

    model.execute(tf.browser.fromPixels(cat));
    pred = model.predict();
}

// refresh grab from model
var refreshbtn = document.getElementById("refresh");
generate();
refreshbtn.addEventListener("click", generate);

// go to next step
var nextbtn = document.getElementById("next");
nextbtn.addEventListener("click", function () {
    var pickup = document.getElementById("pickup");
    localStorage.setItem("pickup", pickup.value)

    location.href = "../steps/step3.html";
});