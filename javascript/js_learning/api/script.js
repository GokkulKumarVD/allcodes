
let button = document.querySelector('.button1');
let header = document.querySelector('.header');

button.addEventListener('click', () => {
    fetch("https://api.adviceslip.com/advice")
        .then(result => result.json())
        .then(data => {
            header.innerText = data.slip.advice;
        });
});