<?php

require 'conn.php';

$empid = htmlspecialchars($_GET['empid']);
$emailid = htmlspecialchars($_GET['emailid']);
$phno = htmlspecialchars($_GET['phno']);

// $empid = '123';
// $emailid = '12@g.com';
// $phno = '12345';



$sql = "insert into couponduplicatedata (empid,emailid,phno)
        values('$empid','$emailid','$phno'); ";
$result = mysqli_query($mysqli, $sql);
