<?php

date_default_timezone_set('Asia/Kolkata');

$epoch = 1633665264;
$dt = new DateTime("@$epoch");  // convert UNIX timestamp to PHP DateTime
echo $dt->format('Y-m-d H:i:s'); // output = 2017-01-01 00:00:00
$dt = $dt->format('Y-m-d H:i:s'); 
