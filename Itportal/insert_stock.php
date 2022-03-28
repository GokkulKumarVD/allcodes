<?php

require 'conn.php';

$laptop_brand = $_GET['laptop_brand'];
$price = $_GET['price'];
$laptop_id = $_GET['laptop_id'];



// $sql = "insert into addstock (laptop_brand,price,laptop_id)
//         values(?,?,?); ";
// $row = $dbo->prepare($sql);
// $row->execute([$laptop_brand, $price, $laptop_id]);


// mysqli
$sql = "insert into addstock (laptop_brand,price,laptop_id,status)
        values('$laptop_brand','$price','$laptop_id','unassigned'); ";
$result = mysqli_query($mysqli, $sql);
