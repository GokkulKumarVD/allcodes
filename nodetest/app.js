var snowflake = require('snowflake-sdk');
var connection = snowflake.createConnection({
    account: 'swiggy-caifuhmyskbpytwlscdfskwp3sfya.global',
    username: 'cc_user@swiggy.in',
    password: '',
    region: ''
});

connection.connect(function(err, conn){
    if (err){
        console.error('unable to connect' + err.message);
    }else{
        console.log('successful' + connection.getId());
    }
})