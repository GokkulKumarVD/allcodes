// it will execute the function one by one

// console.log('start');

// function a1(email) {
//     console.log('inside the function');
//     return new Promise ((resolve, reject) => {
//         setTimeout(() => {
//          return  resolve({ 'email': email });
//         }, 5000);
//     });  

// }



// function a2(name) {
//     console.log('second function');
//     return new Promise ((resolve, reject) => {
//         setTimeout(() => {
//             resolve({'name': name});
//         }, 5000);
//     });
// }

// function a3(title) {
//     console.log('third function');

//     return new Promise ( (resolve, reject) => {
//         setTimeout(() => {
//             resolve({'title': title});
//         }, 5000);

//     });
// }


// const userEmail = a1('gok@g.com');
// const userName = a2('ram'); 
// const userTitle = a3('DS'); 



// console.log('finish');


// another way of callback method-----------------------------------------------------
// it will execute the function one by one. 

// console.log('start');

// function a1(email, callback) {
//     console.log('inside the function');
//         setTimeout(() => {
//             callback({ 'email': email });
//         }, 5000);
// }



// function a2(name, callback) {
//     console.log('second function');
//         setTimeout(() => {
//             callback({'name': name});
//         }, 5000);
// }

// function a3(title, callback) {
//     console.log('third function');

//         setTimeout(() => {
//             callback({'title': title});
//         }, 5000);    
// }

// let user =
//         a1('hi@g', (user) => {
//             console.log(user.email);
//         a2('ram', (user) => {
//             console.log(user.name)
//         a2('DS', (user) => {
//             console.log(user.title)
//         });
//     });
// });




// console.log('finish');



// another callback method using promise.all. it will execute all the functions but result will be shown only after everythin is finished
// let func1 = new Promise((resolve, reject)=> {
//     setTimeout(() => {
//         resolve ('from func1');
//     }, 5000);
// })


// let func2 = new Promise((resolve, reject)=> {
//     setTimeout(() => {
//         resolve ('from func2');
//     }, 5000);
// })

// Promise.all([func1, func2]).then ((result) => console.log(result));



// another best callback method in asyn is this

// console.log('start');

// function a1(email) {
//     console.log('inside the function');
//     return new Promise ((resolve, reject) => {
//         setTimeout(() => {
//          return  resolve({ 'email': email });
//         }, 5000);
//     });  

// }



// function a2(name) {
//     console.log('second function');
//     return new Promise ((resolve, reject) => {
//         setTimeout(() => {
//             resolve({'name': name});
//         }, 5000);
//     });
// }

// function a3(title) {
//     console.log('third function');

//     return new Promise ( (resolve, reject) => {
//         setTimeout(() => {
//             resolve({'title': title});
//         }, 5000);

//     });
// }


// async function displayUser() {
//     try {
//         let user_email = await a1('h$g.com');
//         let user_name = await a2('ram');
//         let user_title = await a3('DS');
//         console.log(user_email.email);
//     } catch (error) {
//         console.log('error');
//     }

// }

// displayUser();