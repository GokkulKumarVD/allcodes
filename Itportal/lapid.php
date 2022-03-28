<?php

require 'conn.php';



$sql = "SELECT laptop_id from addstock";

// $row=$dbo->prepare($sql);
// $row->execute();
// $result = $row-> fetchAll(PDO::FETCH_ASSOC);

// mysqli
$result = mysqli_query($mysqli, $sql);
// Fetch all
mysqli_fetch_all($result, MYSQLI_ASSOC);


$main=array('data'=> $result);

echo json_encode($main);

?>