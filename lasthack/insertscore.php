<?php

require 'conn.php';
session_start();

$_SESSION['timetaken'] = $timetaken;

$emailid = $_GET['emailid'];
$score = $_GET['score'];
$starttime = $_GET['starttime'];
$endtime = $_SERVER['REQUEST_TIME'];
$timetaken = $_GET["timetaken"];

// $emailid = '1@swiggy.in';
// $score = 3;
// $starttime = $_SERVER['REQUEST_TIME'];
// $endtime = $_SERVER['REQUEST_TIME'];

// echo($starttime);

$sql = "update infoquizweek3 set score='$score', starttime='$starttime', endtime='$endtime', timetaken =  '$timetaken' where emailid='$emailid'";
$result = mysqli_query($mysqli, $sql);

// session_unset($_SESSION['empid']);
// session_unset($_SESSION['emailid']);
// session_destroy();
