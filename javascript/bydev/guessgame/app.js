let randomnr = Math.floor(Math.random()*11);

console.log(randomnr);

let guessnumber

do{
    guessnumber = prompt("guess the number between 1 - 10");
}while(guessnumber != randomnr);


console.log('correct number');

