<?php

require 'conn.php';


session_start();

if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];



    if ($username === 'senthil' & $password === 'swiggit') {
        $_SESSION['username'] = $username;
        header("location:dash.php");
    }
}

?>


<html lang="en">

<head>

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">

        <!--Import Google Icon Font-->
        <!-- <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> -->

        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">

        <!--Import Google Icon Font-->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

        <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

        <link rel="stylesheet" href="btnstyle.css">

        <title>Swiggy</title>
    </head>
</head>

<body>
    <div class="card">
        <div class="card-title">
            <h2 class="grey-text center">Login</h2>
        </div>
        <div class="card-content valign center">
            <div class="row">
                <form class="col s12" method="post" autocomplete="off">
                    <div class="row">
                        <div class="input-field col s6">
                            <i class="material-icons prefix">account_circle</i>
                            <input id="username" type="text" class="validate" name="username">
                            <label for="username">User name</label>
                        </div>
                        <div class="input-field col s6">
                            <i class="material-icons prefix">password</i>
                            <input id="password" type="password" class="validate" name="password">
                            <label for="password">Password</label>
                        </div>
                        <div>
                            <input class="waves-effect waves-light btn nb" type="submit" name='submit' value="login">
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script>
        $(document).ready(function() {
            M.updateTextFields();
        });
    </script>
</body>

</html>