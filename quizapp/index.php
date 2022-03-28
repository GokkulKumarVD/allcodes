<?php

require 'conn.php';


session_start();



if (isset($_POST['submit'])) {
    $empid = $_POST['empid'];
    $emailid = $_POST['emailid'];
    $score = '0';
    $starttime = '0';
    $endtime = '0';

    // $a = 'How are you?';
    $search = 'swiggy.in';
    if (preg_match("/{$search}/i", $emailid)) {
        echo 'true';
        $_SESSION['empid'] = $empid;
        $_SESSION['emailid'] = $emailid;

        if (!empty($empid) & !empty($emailid)) {
            $sql = "select * from infoquizlogin where empid=$empid";
            $result = mysqli_query($mysqli, $sql);
            if (mysqli_num_rows($result) == 0) {

                $sql = "insert into infoquizlogin (empid, emailid, score, starttime, endtime) values('$empid','$emailid','$score','$starttime','$endtime'); ";
                $result = mysqli_query($mysqli, $sql);
                header("location:quiz.php");
            } else {
                header("location:alreadytaken.php");
            }

            // header("location:quiz.php");
        } else {
            header("location:validemail.html");
        }
    }
}

?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Latest compiled and minified CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">


    <title>Login quiz</title>
</head>

<body>
    <form action="index.php" method="POST">
        <div class="mb-3">
            <label for="empid" class="form-label">Employee ID</label>
            <input type="text" class="form-control" id="empid" name="empid" required>
        </div>
        <div class="mb-3">
            <label for="emailid" class="form-label">Email ID</label>
            <input type="email" class="form-control" id="emailid" name="emailid" required>
        </div>

        <button type="submit" name='submit' class="btn btn-primary">Submit</button>
    </form>

    <!-- Latest compiled JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

</body>

</html>