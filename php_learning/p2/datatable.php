<?php

$orderid = $_GET['orderid'];
$ordervalue = $_GET['ordervalue'];
$phonenum = $_GET['phonenum'];
$lob = $_GET['lob'];
$segment = $_GET['segment'];
$child = $_GET['child'];

// $orderid = 123;
// $ordervalue = 100;
// $phonenum = 190;
// $lob = 'Food';
// $segment = 'High';
// $child = 'f001';


    require 'conn.php';

    // fetch from table 2
    $sql = "select weightage from table2 where par = '$lob' and cxseg = '$segment'";
    $row = $dbo->prepare($sql);
    $row->execute();
    $result = $row-> fetchAll(PDO::FETCH_ASSOC);
    $weightage = (float)$result[0]['weightage'];
    $cal_result = $ordervalue * $weightage;

    // insert resut to table 3
    $sql = "insert into table3 (order_id, order_val, phone_number, parent, cx_segment, child, calculated_result) 
            values (?,?,?,?,?,?,?);";
    $row = $dbo->prepare($sql);
    $row->execute([$orderid,$ordervalue,$phonenum,$lob,$segment,$child,$cal_result]);


    // fetch the result from table3 and pass it to index function
    $sql = "select order_id, phone_number, calculated_result from table3 order by id desc limit 1;";
    $row=$dbo->prepare($sql);
    $row->execute();
    $result = $row-> fetchAll(PDO::FETCH_ASSOC);

    $main=array('data'=> $result);
    echo json_encode($main);

?>