<?php

require 'conn.php';

$empid = $_GET['empid'];
$email = $_GET['email'];
$approvedby = $_GET['approvedby'];
$assignedby = $_GET['assignedby'];
$laptop = $_GET['laptop'];
// $price = $_GET['price'];
$assigned_date = $_GET['assigneddate'];
$laptopid = $_GET['laptopid'];



// $sql = "insert into itassign (empid,email,approvedby,assignedby,laptop,assigned_date,laptopid)
//         values(?,?,?,?,?,?,?); ";
// $row = $dbo->prepare($sql);
// $row->execute([$empid,$email,$approvedby,$assignedby,$laptop,$assigned_date,$laptopid]);


$sql = "insert into itassign (empid,email,approvedby,assignedby,laptop,assigned_date,laptopid)
        values('$empid','$email','$approvedby','$assignedby','$laptop','$assigned_date','$laptopid'); ";
$result = mysqli_query($mysqli, $sql);






// $sql = "delete from addstock where laptop_id='$laptopid' ";
// $row = $dbo->prepare($sql);
// $row->execute();

// mysqli
$sql = "update addstock set status='assigned' where laptop_id='$laptopid' ";
$result = mysqli_query($mysqli, $sql);


?>