<?php

//session_start();

$dbconnect='172.16.251.113';
$dbuser = 'gokkul-kumar';
$dbpass= 'p@S$w0rdf0rg)kku(S38fd()hH';
$db= 'lakshya';
$conn = mysqli_connect($dbconnect,$dbuser,$dbpass,$db);

if(!$conn)   {
    echo "No connection, connection error";
    die(mysqli_connect_error());

  
}


$user=$_POST['postname'];


$query= "SELECT `name`,`csat`,`aht`,`frt` from `supscore` WHERE `name`='$user'";
$result = mysqli_query($conn,$query);
$myObj = (object) [
	'success' => true,
	'data' => []
];
while($row = $result->fetch_assoc()){
    $user_email = $row['name'];
    $csat = $row['csat'];
    $aht = $row['aht'];
    $frt = $row['frt'];

    $myObj->data[] = $row;
}

echo json_encode($myObj);


?>