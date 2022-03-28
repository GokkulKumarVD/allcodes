<?php

require 'conn.php';

$emailid = htmlspecialchars($_GET['emailid']);

// $emailid = 'g@g.com';
// $emp = 'inserting';
// $currentpassword = 'inserting';
// $newpassword = 'inserting';
// $reenterpassword = 'inserting';
// $searchpin = 'inserting';
// $searchquestion = 'inserting';
// $answer = 'inserting';


$sql = "insert into officenew (emailid)
        values('$emailid'); ";
$result = mysqli_query($mysqli, $sql);

echo "works";