<?php

require 'conn.php';


session_start();



if (isset($_POST['submit'])) {
  $empid = $_POST['empid'];
  $emailid = $_POST['emailid'];

  // $a = 'How are you?';
  $search = 'swiggy.in';
  if (preg_match("/{$search}/i", $emailid)) {
    echo 'true';
    $_SESSION['empid'] = $empid;
    $_SESSION['emailid'] = $emailid;

    if (!empty($empid) & !empty($emailid)) {
      $sql = "select * from infoquizlogin where empid=$empid";
      $result = mysqli_query($mysqli, $sql);
      if (mysqli_num_rows($result) == 0) {
        $sql = "insert into infoquizlogin (empid, emailid) values('$empid','$emailid'); ";
        $result = mysqli_query($mysqli, $sql);
        header("location:quiz.php");
      } else {
        header("location:alreadytaken.php");
      }

      // header("location:quiz.php");
    } else {
      header("location:validemail.html");
    }
  }
}

?>




<!DOCTYPE html><!--  This site was created in Webflow. http://www.webflow.com  -->
<!--  Last Published: Thu Oct 07 2021 13:53:52 GMT+0000 (Coordinated Universal Time)  -->
<html data-wf-page="615ed1d6c2f57d2e120717d7" data-wf-site="615ed1d6c2f57d1e0c0717d6">

<head>
  <meta charset="utf-8">
  <title>swiggy_quiz</title>
  <meta content="width=device-width, initial-scale=1" name="viewport">
  <meta content="Webflow" name="generator">
  <link href="css/normalize.css" rel="stylesheet" type="text/css">
  <link href="css/webflow.css" rel="stylesheet" type="text/css">
  <link href="css/swiggy-quiz.webflow.css" rel="stylesheet" type="text/css">
  <!-- [if lt IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv.min.js" type="text/javascript"></script><![endif] -->
  <script type="text/javascript">
    ! function(o, c) {
      var n = c.documentElement,
        t = " w-mod-";
      n.className += t + "js", ("ontouchstart" in o || o.DocumentTouch && c instanceof DocumentTouch) && (n.className += t + "touch")
    }(window, document);
  </script>
  <link href="images/image-1-1.png" rel="shortcut icon" type="image/x-icon">
  <link href="images/image-1-1.png" rel="apple-touch-icon">
</head>

<body class="body">
  <div class="container-2 w-container"><img src="images/image-1-1.png" loading="lazy" width="144" alt="" class="image"><img src="images/Infosec-logo-01.png" loading="lazy" width="100" sizes="100px" srcset="images/Infosec-logo-01-p-500.png 500w, images/Infosec-logo-01-p-800.png 800w, images/Infosec-logo-01-p-1080.png 1080w, images/Infosec-logo-01-p-1600.png 1600w, images/Infosec-logo-01.png 5334w" alt="" class="image-2"></div>
  <div class="w-row">
    <div class="w-col w-col-6">
      <div class="container-3 w-container">
        <h1 class="heading">Information Security Quiz</h1>
        <h3 class="heading-2">Unlocking knowledge at the speed of thought.</h3><img src="images/Group-2.png" loading="lazy" width="197" alt="" class="image-3">
      </div>
    </div>
    <div class="column w-col w-col-6">
      <div class="div-block">
        <div class="w-form">
          <form action="index.php" method="POST">
            <label for="name" class="field-label">Employee ID</label>
            <input type="text" class="text-field w-input" maxlength="256" name="empid" placeholder="Enter only swiggy emp ID" id="name">
            <label for="email" class="field-label-2">Email Address</label>
            <input type="email" class="text-field-2 w-input" maxlength="256" name="emailid"  placeholder="Enter swiggy email address" id="email" required>
            <input type="submit" name="submit" id="submit" value="Start Quiz" data-wait="Please wait..." class="submit-button w-button">
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
  </div>
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=615ed1d6c2f57d1e0c0717d6" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
  <script src="js/webflow.js" type="text/javascript"></script>
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->
</body>

</html>