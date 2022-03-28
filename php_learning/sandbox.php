<?php

if(isset($_POST['submit'])){
    session_start();
    $_SESSION['name'] = $_POST['name'];
    header('location:index.php');
    
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
    <div class="container">
    <form action="sandbox.php" method="post">
        <input type="text" name="name">
        <input type="submit" name='submit' class="btn">
    </form>
    </div>
</body>

</html>