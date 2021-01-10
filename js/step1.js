// block page reload
var form = document.getElementById("form");
form.addEventListener('submit', function (event) { event.preventDefault(); });

// disabling form submissions if there are invalid fields
function checkValid() {
    var elements = document.getElementById("form").elements;

    var valid = true;
    for (var i = 0, element; element = elements[i++];) {
        if (element.classList.contains("form-control") && element.value === "") {
            valid = false;
            break;
        }
    }

    return valid;
}

// save info to local storage
var submitbtn = document.getElementById("submit");

submitbtn.addEventListener("click", function () {
    if (!checkValid()) {
        return;
    }

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