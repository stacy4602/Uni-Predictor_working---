let circularProgress = document.querySelector(".circular-progress"),
progressValue = document.querySelector("span.progress-value");
const y=document.getElementsByClassName("progress-value")
let progressStartValue = -1,    
progressEndValue = y[0].innerHTML,    
speed = 50;

let progress = setInterval(() => {
progressStartValue++;

progressValue.textContent = `${progressStartValue}%`
circularProgress.style.background = `conic-gradient(#0372a5 ${progressStartValue * 3.6}deg, #ededed 0deg)`

if(progressStartValue == progressEndValue){
    clearInterval(progress);
}    
}, speed);