// store it in local storage
// localStorage.setItem("baby","boy");

//it will overwrite if it has same name
// localStorage.setItem("baby","girl");


// session storage
// sessionStorage.setItem("baby", "boy")

// unset storage
// sessionStorage.removeItem("baby");

// get value from local storage
// let local = localStorage.getItem("baby");
// console.log(local)

// storing array to local storage and reading from local storage
lovers = ['gokkul','sujitha'];
localStorage.setItem("couple",JSON.stringify(lovers));

let sex = JSON.parse(localStorage.getItem("couple"));
console.log(sex);
