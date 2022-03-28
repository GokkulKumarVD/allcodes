<?php

include 'conn.php';

if(isset($_POST['delete'])){
    $id = mysqli_real_escape_string($conn, $_POST['id_to_delete']);

    $sql = "delete from nizza_pizza WHERE id = $id";

    if(mysqli_query($conn, $sql)){
        echo 'success';
        header('location: index.php');
    }{
        echo mysqli_error($conn);
    }

}



if (isset($_GET['id'])) {

    $id = $_GET['id'];

    $id = mysqli_real_escape_string($conn, $_GET['id']);

    $sql = "SELECT * from nizza_pizza WHERE id = $id";

    $resut = mysqli_query($conn, $sql);

    $pizzas = mysqli_fetch_assoc($resut);

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

    <?php include('header.php') ?>


    <div class="container center">
        <h2><?php echo $pizzas['email'] ?></h2>
        <form action="details.php" method="post">
            <input type="hidden" name="id_to_delete" value="<?php echo $pizzas['id'] ?>">
            <input type="submit" name="delete" class="btn brand" value="delete">
        </form>
    </div>

</body>

</html>