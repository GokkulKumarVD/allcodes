// store in local storage
localStorage.setItem('name' , 'ram');
localStorage.setItem('age', 50);

// get data
let name = localStorage.getItem('name');
let age = localStorage.getItem('age');

console.log(name, age);

// delete data
localStorage.removeItem('name');


// delete all
localStorage.clear();



