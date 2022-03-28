// let v = 10;


// switch (v) {
//     case 10:
//         console.log("first");
//         break;
//     default:
//         console.log("end");
// }

// lt = ['a', 'b', 'c', 'd'];
// let element = ``;

// let cname = document.querySelector(".thisone");

// for (let index = 0; index < lt.length; index++) {
//      element += `<li>${lt[index]}</li>`;
// }

// // lt.forEach(function(lst){
// //     element += `<li>${lst}</li>`;
// // })


// // lt.forEach((el) => {
// //     element += `<li style="color:purple">${el}</li>`;
// // });

// console.log(element);
// cname.innerHTML = element;



// let obj = {
//     lst : ['a','b'],
//     name : 'ram'
// }

// console.log(obj.lst[1]);

// ---------------------------
// let para = document.querySelector('p');

// para.innerText +='apple';

// console.log(para.innerText);

// let col = document.querySelector('.hry');
// col.setAttribute('style','color:green');


// const lst = document.querySelectorAll('li');

// const ul = document.querySelector('ul');
// const btn = document.querySelector('button')

// btn.addEventListener('click', function(){
//     // ul.innerHTML += `<li> new one </li>`;
//     const le = document.createElement('li');
//     le.textContent='adding it';
//     // ul.append(le);
//     ul.prepend(le);
// });


// lst.forEach(element => {
//     element.addEventListener('click', function (e) {
//         console.log(`you cancelled ${element.textContent}`);
//         // e.target.style.textDecoration = 'line-through';
//         console.log('event in li')
//         e.stopPropagation();
//         e.target.remove();
//     });
// });

// ul.addEventListener('click', (e) => {
//     console.log(e);
//     if(e.target.tagName === 'LI'){
//         e.target.remove();
//     }
// })




// const usern = document.querySelector('.form-signup');
// const usernval = document.querySelector('#username');

// usern.addEventListener('submit', (e) => {
//     e.preventDefault();
//     console.log(usernval.value)
// });



let correctAnswer = ['C','C','D','D','D','A','D','D','A','A'];

let form = document.querySelector('.quiz-form');
let result = document.querySelector('.result');

form.addEventListener('submit', (e)=> {
    e.preventDefault();
    result.style.display = 'block';

    let score = 0;
    
    let userAnswer = [form.opt.value, 
        form.opt1.value, form.opt2.value, form.opt3.value, form.opt4.value,  form.opt5.value, form.opt6.value, form.opt7.value, 
        form.opt8.value,  form.opt9.value];
    console.log(userAnswer)

    userAnswer.forEach((element, index) => {
        if (element === correctAnswer[index]){
            score += 1;
        }
    });    

    scrollTo(0,0);
    result.classList.remove('d-none');

    let output = 0;
    let tm = setInterval( () => {
        result.querySelector('span').textContent=`${output}/10`;
        if (output === score) {
            clearInterval(tm);
        }else{
            output++;
        }

    }, 100)  

});