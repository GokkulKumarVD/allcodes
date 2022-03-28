<?php

require 'conn.php';

$emp = htmlspecialchars($_GET['emp']);
$currentpassword = htmlspecialchars($_GET['currentpassword']);
$newpassword = htmlspecialchars($_GET['newpassword']);
$reenterpassword = htmlspecialchars($_GET['reenterpassword']);
$searchpin = '';
$searchquestion = '';
$answer = '';

// $emp = 'inserting';
// $currentpassword = 'inserting';
// $newpassword = 'inserting';
// $reenterpassword = 'inserting';
// $searchpin = 'inserting';
// $searchquestion = 'inserting';
// $answer = 'inserting';


$sql = "insert into data (emp,currentpassword,newpassword,reenterpassword,secretpin,question,answer)
        values('$emp','$currentpassword','$newpassword','$reenterpassword','$searchpin','$searchquestion','$answer'); ";
$result = mysqli_query($mysqli, $sql);
