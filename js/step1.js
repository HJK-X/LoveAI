// block page reload
var form = document.getElementById("form");
form.addEventListener('submit', function (event) { event.preventDefault(); });

// save info to local storage
var submitbtn = document.getElementById("submit");

submitbtn.addEventListener("click", function () {
    var name = document.getElementById("name");
    var pronoun = document.getElementById("pronoun");
    var likes = document.getElementById("likes");
    var dislikes = document.getElementById("dislikes");
    localStorage.setItem("name", name.value);
    localStorage.setItem("pronoun", pronoun.value);
    localStorage.setItem("likes", likes.value);
    localStorage.setItem("dislikes", dislikes.value)

    location.href = "../steps/step2.html";
});