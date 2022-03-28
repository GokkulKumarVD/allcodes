// let users = ['Gokkul','sujitha','kid'];



// advantage is: we can put if conditions inside this loop wherein 
// for earch loop does not work with if condition inside
// for (let user of users){
    
//     if(user === 'kid'){
//         console.log('no kid, only sex');
//         continue;
//     }
//     console.log(user);
// }



// ---------------------------------------------------------------------
// mostly used for arrays and if conditions will not work inside this
// users.forEach(element => {
//     console.log(element);
    
// });


// ---------------------------------------------------------------------
// "for in" loop used to loop through objects

let user = {
    name : 'Gokkul',
    subscribed : 'yes',
    plan : 'premium'
}


for (let e in user){
    console.log(user[e]);
}