<?php
session_start();

if (isset($_SESSION['views']))
    $_SESSION['views'] = $_SESSION['views'] + 1;
else
    $_SESSION['views'] = 1;

$count = $_SESSION['views'];

require 'conn.php';

$sql = "insert into ransomeware (count)
        values('$count'); ";
$result = mysqli_query($mysqli, $sql);

session_destroy();

?>
<!DOCTYPE html>
<!--  This site was created in Webflow. http://www.webflow.com  -->
<!--  Last Published: Wed Oct 13 2021 06:10:46 GMT+0000 (Coordinated Universal Time)  -->
<html
  data-wf-page="616675e0196ee9b0544021b1"
  data-wf-site="616675e0196ee96bfc4021b0"
>
  <head>
    <meta charset="utf-8" />
    <title>SwiggyRansomeware</title>
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <meta content="Webflow" name="generator" />
    <link href="css/normalize.css" rel="stylesheet" type="text/css" />
    <link href="css/webflow.css" rel="stylesheet" type="text/css" />
    <link
      href="css/swiggyransomeware.webflow.css"
      rel="stylesheet"
      type="text/css"
    />
    <!-- [if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif] -->
    <script type="text/javascript">
      !(function (o, c) {
        var n = c.documentElement,
          t = " w-mod-";
        (n.className += t + "js"),
          ("ontouchstart" in o ||
            (o.DocumentTouch && c instanceof DocumentTouch)) &&
            (n.className += t + "touch");
      })(window, document);
    </script>
    <link href="images/swiggy.svg" rel="shortcut icon" type="image/x-icon" />
    <link href="images/swiggy.svg" rel="apple-touch-icon" />
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet" />
  </head>
  <body class="body">
    <div class="container w-container">
      <h3 class="heading">
        Your system has been hacked. Please contact infosec@swiggy.in or reach
        out to 080-45691286
      </h3>
    </div>
    <div class="container-2 w-container" id="attackBox">
      <div class="text-block" id="attackText" data-aos="zoom-in-up">
        Your system is under Attack !
      </div>
      <div class="text-block" id="attackText" data-aos="zoom-in-right">
        Your system is under Attack !
      </div>
      <div class="text-block" id="attackText" data-aos="zoom-in-down">
        Your system is under Attack !
      </div>
      <div class="text-block" id="attackText" data-aos="zoom-in-left">
        Your system is under Attack !
      </div>
    </div>
    <script src="./js/script.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
      AOS.init();
    </script>
    <script
      src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=616675e0196ee96bfc4021b0"
      type="text/javascript"
      integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
      crossorigin="anonymous"
    ></script>
    <script src="js/webflow.js" type="text/javascript"></script>
    <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->
  </body>
</html>
