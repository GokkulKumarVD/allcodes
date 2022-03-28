<?php

$servername = "localhost";
$username = "gokkul";
$password ="php_learning";
$db = "phish";


// $servername = "";
// $username = "root";
// $password ="b@rlin!#23^";
// $db = "phish";

// try {
//     $dbo = new PDO('mysql:host='.$servername.';dbname='.$db, $username, $password);
//     } 
// catch (PDOException $e) {
//     print "Error!: " . $e->getMessage() . "<br/>";
// die();
//     }


$mysqli = new mysqli($servername,$username,$password,$db);

if ($mysqli -> connect_errno) {
    echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
    exit();
  }


?>