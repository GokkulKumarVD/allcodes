<?php

session_start();

session_unset($_SESSION['empid']);
session_unset($_SESSION['emailid']);
session_destroy();
header("location:index.php");


?>
