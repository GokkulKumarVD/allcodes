<?php

require 'conn.php';

// $laptop_brand = $_GET['laptop_brand'];
// $price = $_GET['price'];
// $laptop_id = $_GET['laptop_id'];

$laptop_brand = 'dell';

$sql = "SELECT assigned_laptop.assigned, unassigned.unassigned_laptop
        FROM 
        ( SELECT COALESCE(COUNT(laptop),0) AS assigned  
        FROM itassign where laptop = '$laptop_brand' ) assigned_laptop,
        ( SELECT COALESCE(COUNT(laptop_brand),0) as unassigned_laptop
        FROM addstock WHERE laptop_brand = '$laptop_brand' and status='unassigned' ) unassigned";

// $row=$dbo->prepare($sql);
// $row->execute();
// $result = $row-> fetchAll(PDO::FETCH_ASSOC);


// mysqli
$result = mysqli_query($mysqli, $sql);
// Fetch all
// mysqli_fetch_all($result, MYSQLI_ASSOC);
$row = mysqli_fetch_all($result, MYSQLI_ASSOC);


$main=array('data'=> $row);

echo json_encode($main);

?>