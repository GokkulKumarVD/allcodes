<?php

$lob = $_GET['lob'];

// $lob = "Food";

require 'conn.php';

$sql = "select child from table1 where prt = '$lob' ;";
$row=$dbo->prepare($sql);
$row->execute();
$result = $row-> fetchAll(PDO::FETCH_ASSOC);

$main=array('data'=> $result);

echo json_encode($main);

?>