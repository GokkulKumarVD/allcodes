<?php

include 'conn.php';

if(isset($_POST['submit'])){
    $f_name = $_POST['first_name'];
    $s_name = $_POST['second_name'];
    $email = $_POST['email'];
    $pizzatitle = $_POST['pizzatitle'];
    $ingredients = $_POST['ingredients'];

    $sql = "INSERT INTO nizza_pizza (first_name,second_name,email,title,ingredients) VALUES ('$f_name', '$s_name', '$email'
    , '$pizzatitle', '$ingredients')";

    echo("$f_name");

    if(mysqli_query($conn, $sql)){
        // success
        header('Location: index.php');
    } else {
        echo 'query error: '. mysqli_error($conn);
    }

}

?>


<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<?php include("header.php") ?>

<form action="add.php" method="POST">
        <div class="container">
            <div class="row">
                <div class="input-field col s12 l6">
                    <input type="text" name="first_name">
                    <label class="subtext" for="first_name">First name</label>
                </div>
                <div class="input-field col s12 l6">
                    <input type="text" name="second_name">
                    <label class="subtext" for="second_name">Second name</label>
                </div>
                <div class="input-field col s12 l12">
                    <input type="email" name="email">
                    <label class="subtext" for="email">Email</label>
                </div>
                <div class="input-field col s12 l12">
                    <input type="text" name="pizzatitle">
                    <label class="subtext" for="pizzatitle">Pizza title</label>
                </div>
                <div class="input-field col s12 l12">
                    <input type="text" name="ingredients">
                    <label class="subtext" for="ingredients">Ingredients</label>
                </div>
            </div>
            <div class="input-field center">
                <button class="btn" type="submit" name="submit">Submit</button>
            </div>
        </div>
    </form>
</body>