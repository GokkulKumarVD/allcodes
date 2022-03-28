<?php

$servername = "localhost";
$username = "gokkul";
$password ="php_learning";
$db = "proj2";

try {
    $dbo = new PDO('mysql:host='.$servername.';dbname='.$db, $username, $password);
    } 
catch (PDOException $e) {
    print "Error!: " . $e->getMessage() . "<br/>";
die();
    }

?>
