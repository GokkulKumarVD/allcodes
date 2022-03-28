// html selector is fast and it will not fetch comment and text. it will fetch only elements
// "for each" loop will not work on html selector
// let headers = document.getElementsByTagName('h2');
// console.log(headers);

// -------------

// query selector is slow and it will fetch comment and text etc.,
// "for each" will work on query selector
// let headers = document.querySelectorAll("h2");
// console.log(headers);


// ------------


// it is nodelist
// let child = document.querySelector('#list')
// console.log(child.childNodes);

// -------------

// here we fetch only elements, it becomes html elements
// let child = document.querySelector('#list')
// console.log(child.children);

// ------------------

// add new item 6
// let lists = document.querySelector('#list');
// let items = lists.children;

// let newelement = document.createElement('li');
// newelement.classList.add('item');
// newelement.innerText="Item 6";

// lists.appendChild(newelement);


// ----------
// add new items by clicking on submit button
let submit = document.querySelector("#submit");
let todolist = document.querySelector("#list");
let listnumber = todolist.children;
let items = document.querySelectorAll(".item")
let inputvalue = document.querySelector(".inputvalue")

submit.addEventListener("click", function(e){
    // stops normal behavior of browser
    e.preventDefault();

    // create element
    let newitem = document.createElement('li');
    
    // add class name
    newitem.classList.add('item');

    // input values to elemet
    newitem.innerText = `${inputvalue.value}`;
    
    // append new item to parent element
    todolist.appendChild(newitem);

    // adding delete events to new item
    newitem.addEventListener("click", function(e){
        e.target.remove();
    })

    inputvalue.value = "";
   
});

// adding events to already created items
for(item of items){
    item.addEventListener("click", function(e){
        e.target.remove();
    });
}

