// classes / chaining methods 


class user {
    constructor(username, email){
        this.username = username;
        this.email = email;
        this.score = 0;
    }
    login(){
        console.log(`${this.username} has logged in!`);
        return this;
    }
    incscore(){
        this.score += 1;
        console.log(`the score is ${this.score}`);
        return this;
    }
    logout(){
        console.log(`${this.username} has logged out!`);
        return this;
    }
}

class admin extends user {
    constructor(username, email, boss){
        super(username, email);
        this.title = 'boss';
    }

    delete_(user_name){
        users = users.filter( (u) => {
            return u.username !== user_name.username; 
        });
    }
}





let userOne = new user('gokkul','g@gmail.com');
let userTwo = new user('sujitha','s@gmail.com');
let userThree = new user('mohan','m@mail.com');
let admin_ = new admin('admin_person','ad@mail.com','boss');


admin_.delete('admin_person')


// let users = [userOne, userTwo, userThree];
// console.log(users);

//when you want to execute particular method in the class 
// admin_.delete_(userThree);
// console.log(users);

console.log(userThree);




// method chaining - method must return something to use chaining method
// userOne.login().incscore();
// userTwo.incscore();



// inheritance - it will take constructor from the parent class only if there is no constructor in the inherited class