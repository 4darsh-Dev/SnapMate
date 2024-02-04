console.log("I am working fine!");


// Loader Configuration
let preloadoer = document.getElementById('preloader');

// window.addEventListener("load", function(){
//     preloadoer.style.display = "none";

// })

setTimeout(() => {
    // 
    preloadoer.style.transition = "opacity 0.5s";
    preloadoer.style.opacity = "0";
    preloadoer.style.display = "none";

}, 3000);