let addForm = document.querySelector('.add');
let list = document.querySelector('.todos');
let search = document.querySelector('.search input');

let generatetemplates = (todo) => {
    let html = `
    <li class="list-group-item d-flex justify-content-between align-items-center">
                <span> ${todo} </span>
                <i class="far fa-trash-alt delete"></i>
            </li>
    `
    list.innerHTML += html;
};


addForm.addEventListener('submit', (e) => {
    e.preventDefault();
    todo = addForm.add.value.trim();
    if (todo.length) {
        generatetemplates(todo);
        addForm.reset();
    }else{
        console.log('enter the value');
    }

});

// ------delete todo

list.addEventListener('click', (e)=> {
    if (e.target.classList.contains('delete')) {
        e.target.parentElement.remove();
    }
});

// search

const fnd = (term) => {
    // console.log(list.children);
    Array.from(list.children)
    .filter((todo) => !todo.textContent.toLowerCase().includes(term))
    .forEach((todo) => todo.classList.add('filtered'));


    Array.from(list.children)
    .filter((todo) => todo.textContent.toLowerCase().includes(term))
    .forEach((todo) => todo.classList.remove('filtered'));
    

};


search.addEventListener('keyup', ()=>{
    let term = search.value.trim().toLowerCase();
    fnd(term);
})

