let crossBtn = document.getElementById("cross-btn");
let errorMsgElem = document.getElementById("error-message");

crossBtn.addEventListener("click", function () {
    errorMsgElem.style.display = "none";

})

document.addEventListener("DOMContentLoaded", function () {

    // Setting timeout for n Seconds
    setTimeout(() => {
        if (errorMsgElem) {
            errorMsgElem.style.display = "none";
        }
    }, 5000);


})

