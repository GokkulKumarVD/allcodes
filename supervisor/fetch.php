<?php

//session_start();
$dbconnect='localhost';
$dbuser = 'root';
$dbpass= '';
$db= 'access';
$conn = mysqli_connect($dbconnect,$dbuser,$dbpass,$db);

if(!$conn)   {
    echo "No connection, connection error";
    die(mysqli_connect_error());

  
}


$parent_category_id = 

?>