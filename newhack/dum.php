<?php



require "conn.php";


mysqli_select_db($mysqli, 'phish');
$sql = "SELECT empid,emailid,phno from couponduplicatedata;";
$setRec = mysqli_query($mysqli, $sql);
$columnHeader = '';
$columnHeader = "empid" . "\t" . "emailid" . "\t" . "phno" . "\t";
$setData = '';
while ($rec = mysqli_fetch_row($setRec)) {
    $rowData = '';
    foreach ($rec as $value) {
        $value = '"' . $value . '"' . "\t";
        $rowData .= $value;
    }
    $setData .= trim($rowData) . "\n";
}

header("Content-type: application/octet-stream");
header("Content-Disposition: attachment; filename=User_Detail.xls");
header("Pragma: no-cache");
header("Expires: 0");

echo ucwords($columnHeader) . "\n" . $setData . "\n";
