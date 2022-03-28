<?php

require 'conn.php';
session_start();


$emailid = $_GET['emailid'];
$score = $_GET['score'];
$starttime = $_GET['starttime'];
$endtime = $_SERVER['REQUEST_TIME'];

// $emailid = '1@swiggy.in';
// $score = 3;
// $starttime = $_SERVER['REQUEST_TIME'];
// $endtime = $_SERVER['REQUEST_TIME'];

// echo($starttime);

$sql = "update infoquizlogin set score='$score', starttime='$starttime', endtime='$endtime' where emailid='$emailid'";
$result = mysqli_query($mysqli, $sql);

// session_unset($_SESSION['empid']);
// session_unset($_SESSION['emailid']);
// session_destroy();
