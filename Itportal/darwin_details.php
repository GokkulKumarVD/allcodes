<?php

require 'conn.php';

$empid = $_GET['empid'];

// $empid = 107;

$sql = "select * from darwin where empid = '$empid';";

// mysqli
$result = mysqli_query($mysqli, $sql);
// Fetch all
// mysqli_fetch_all($result, MYSQLI_ASSOC);
$row = mysqli_fetch_all($result, MYSQLI_ASSOC);

$main=array('data'=> $row);

echo json_encode($main);

?>