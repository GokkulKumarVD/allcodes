<?php
//session_start();

$dbconnect='172.16.251.113';
$dbuser = 'gokkul-kumar';
$dbpass= 'p@S$w0rdf0rg)kku(S38fd()hH';
$db= 'lakshya';
$conn = mysqli_connect($dbconnect,$dbuser,$dbpass,$db);

if(!$conn)   {
    echo "No connection, connection error";
    die(mysqli_connect_error());

  
}

$x = $_POST['postname'];

$query = "SELECT `EMAIL_ID` from `manager_mapping` WHERE `REPORTS_TO`='$x'";
$result = mysqli_query($conn,$query);

$myObj = (object) [
    'success' => true,
    'data' => []
];
while($row = $result->fetch_assoc()){

        $temp = $row['EMAIL_ID'];

            $myObj->data[] = $row;
        }

       





echo json_encode($myObj);
//echo $x;


?>