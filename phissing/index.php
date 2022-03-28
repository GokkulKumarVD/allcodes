<?php
session_start();

if (isset($_SESSION['views']))
  $_SESSION['views'] = $_SESSION['views'] + 1;
else
  $_SESSION['views'] = 1;

$count = $_SESSION['views'];

require 'conn.php';

$sql = "insert into officenewcount (count)
        values('$count'); ";
$result = mysqli_query($mysqli, $sql);


// if (isset($_POST['submit'])) {

//   header("Location: hackv.php");
// }

// if (isset($_POST['submit'])) {

//   $contains = "swiggy.in";

//   $email = $_POST['emailid'];

//   // or use (as outlined below)
//   // if(isset($_POST['email']) && preg_match("/\b(@gmail.com)\b/", $_POST['email']))

//   if (isset($_POST['emailid']) && preg_match("/\b($contains)\b/", $email)) {
//     header("Location: hackv.php");
//   } else {
//     echo 'invalid input!';
//   }
// }


session_destroy();

?>



<!DOCTYPE html><!--  This site was created in Webflow. http://www.webflow.com  -->
<!--  Last Published: Wed Oct 06 2021 06:55:53 GMT+0000 (Coordinated Universal Time)  -->
<html data-wf-page="615c9294661107765933cf13" data-wf-site="615c9294661107dcaf33cf12">

<head>
  <meta charset="utf-8">
  <title>Swiggy office workspace</title>
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta content="Webflow" name="generator">
  <link href="css/normalize.css" rel="stylesheet" type="text/css">
  <link href="css/webflow.css" rel="stylesheet" type="text/css">
  <link href="css/swiggy-coupon.webflow.css" rel="stylesheet" type="text/css">
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
  <script type="text/javascript">
    WebFont.load({
      google: {
        families: ["Open Sans:300,300italic,400,400italic,600,600italic,700,700italic,800,800italic"]
      }
    });
  </script>
  <!-- [if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif] -->
  <script type="text/javascript">
    ! function(o, c) {
      var n = c.documentElement,
        t = " w-mod-";
      n.className += t + "js", ("ontouchstart" in o || o.DocumentTouch && c instanceof DocumentTouch) && (n.className += t + "touch")
    }(window, document);
  </script>
  <link href="images/favicon.ico" rel="shortcut icon" type="image/x-icon">
  <link href="images/webclip.png" rel="apple-touch-icon">
  <style>
    .container {
      height: 150px !important;
      margin-top: 90px !important;
      /* max-width: 260px;
    padding-right: 20px;
    padding-left: 20px;
    border-radius: 10px;
    background-color: rgba(240, 135, 6, 0.15);
    color: rgba(240, 135, 6, 0.15); */
    }

    .heading {
      background-color: #fff;
      font-family: 'Open Sans', sans-serif;
      color: #e69138;
      font-weight: 700;
      padding-left: 120px !important;
      padding-right: 24px;
      padding-top: 24px !important;
    }
  </style>
</head>

<body class="body">
  <div class="w-row">
    <div class="column-2 w-col w-col-6"><img src="images/Swiggy.svg" loading="lazy" alt="">
      <h1 class="heading">Excited to know where we’re moving? Please enter your swiggy email id</h1>
      <div class="container w-container">
        <div class="w-form">
          <form method="post">

            <label for="name-3" class="field-label"></label>
            <input type="text" class="text-field w-input" maxlength="256" name="emailid" placeholder="&nbsp; Swiggy Email address" id="emailid">

            <input type="submit" value="Submit" id="submit" name="submit" data-wait="Please wait..." class="submit-button w-button">
          </form>
          <!-- <div class="w-form-done">
            <div>Thank you! Your submission has been received!</div>
          </div> -->
          <!-- <div class="w-form-fail">
            <div>Oops! Something went wrong while submitting the form.</div>
          </div> -->
        </div>
      </div>
    </div>
    <div class="column w-col w-col-6">
      <h1 class="heading-2">It’s time to move on to a new place!</h1><img src="images/success-1.png" loading="lazy" alt="" class="image-2">
      <!-- <h1 class="heading-3">It’s time to move to a new place!</h1> -->
    </div>
  </div>
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=615c9294661107dcaf33cf12" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
  <script src="js/webflow.js" type="text/javascript"></script>
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->

  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
  <script>
    $(document).ready(function() {


      $('#submit').click(function() {
        var emailid = $('#emailid').val();


        if ($('#emailid').val().length === 0 || !emailid.includes('swiggy.in')) {
          alert('Enter swiggy email address');
        } else {
          $.get('insert.php', {
            'emailid': emailid

          }, function() {

            console.log('worked');
          }, "json");



          $('#emailid').val("");

          console.log('working')



          location.replace("hackv.php")

          // use the following code if the above code does not work but you must give entire location includes http
          // window.location = "http://www.swiggy.com";



        }
      })
    });
  </script>



</body>

</html>