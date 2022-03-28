<?php

require 'conn.php';

$searchby = $_GET['searchby'];

if($searchby==='laptopid'){
    $details = $_GET['details'];
}else{
    $details = $_GET['details'];
$selected = $_GET['selected'];
}



// $searchby = 'laptopid';
// $details = 'SWLP5011339';
// $selected = 'seggregate';


if($searchby == 'laptopid'){
    $sql = "SELECT itassign.email, itassign.assignedby, itassign.approvedby, darwin.work_location, 	
                darwin.grade, LEFT(from_unixtime(floor(itassign.assigned_date/1000)),10) as assigned_date, addstock.price
                FROM itassign 
                LEFT JOIN darwin ON 
                itassign.email = darwin.email 
                LEFT JOIN addstock ON
                itassign.laptopid = addstock.laptop_id
                WHERE itassign.laptopid = '$details';";
}elseif($searchby == 'assignedby' && $selected == 'complete'){
    $sql = "SELECT itassign.email, itassign.approvedby, darwin.work_location, darwin.grade, 
            LEFT(from_unixtime(floor(itassign.assigned_date/1000)),10) as assigned_date, addstock.price
            FROM itassign 
            LEFT JOIN darwin ON 
            itassign.email = darwin.email 
            LEFT JOIN addstock ON
                itassign.laptopid = addstock.laptop_id
            WHERE itassign.assignedby = '$details';";
}elseif($searchby == 'assignedby' && $selected == 'seggregate'){
    $sql = "SELECT assignedby, COUNT(laptop) as count FROM itassign
            WHERE assignedby = '$details'
            GROUP BY 1;";
}



// pdo
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