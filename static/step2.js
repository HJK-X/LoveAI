/*
const MODEL_URL = 'model_directory/model.json';

const model = await tf.loadGraphModel(MODEL_URL);


// prep to generate samples
const lines = [];
const name = localStorage.getItem("name");
const pronoun = localStorage.getItem("pronoun");
const likes = localStorage.getItem("likes");
const dislikes = localStorage.getItem("dislikes");

const input = name + " " + pronoun + " " + likes + " " + dislikes;

function generate() {
    pred = model.predict(input);

    lines.push(pred);
}

function refresh() {
    var line = lines.pop();

    var pickup = document.getElementById("pickup");
    pickup.innerText = line;

    if (lines.length == 0) {
        generate();
    }
}

// refresh grab from model
generate();
var refreshbtn = document.getElementById("refresh");
refreshbtn.addEventListener("click", refresh);
*/