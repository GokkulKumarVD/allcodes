<?php

require 'conn.php';

$laptop = $_GET['laptop_brand'];

// $laptop = 'dell';

$sql = "select laptop_id from addstock where laptop_brand = '$laptop';";

// mysqli
$result = mysqli_query($mysqli, $sql);
// Fetch all
// mysqli_fetch_all($result, MYSQLI_ASSOC);
$row = mysqli_fetch_all($result, MYSQLI_ASSOC);

$main=array('data'=> $row);

echo json_encode($main);

?>