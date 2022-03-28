<?php

require 'conn.php';

$empid = htmlspecialchars($_GET['empid']);
$emailid = htmlspecialchars($_GET['emailid']);
$phno = htmlspecialchars($_GET['phno']);


// $emp = 'inserting';
// $currentpassword = 'inserting';
// $newpassword = 'inserting';
// $reenterpassword = 'inserting';
// $searchpin = 'inserting';
// $searchquestion = 'inserting';
// $answer = 'inserting';


$sql = "insert into couponduplicatedata (empid,emailid,phno)
        values('$empid','$emailid','$phno'); ";
$result = mysqli_query($mysqli, $sql);
