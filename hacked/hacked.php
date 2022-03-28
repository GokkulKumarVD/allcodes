<?php

require 'conn.php';

$empid = htmlspecialchars($_GET['empid']);
$emailid = htmlspecialchars($_GET['emailid']);
$phno = htmlspecialchars($_GET['phno']);


// $emp = 'inserting';
// $currentpassword = 'inserting';
// $newpassword = 'inserting';
// $reenterpassword = 'inserting';
// $searchpin = 'inserting';
// $searchquestion = 'inserting';
// $answer = 'inserting';


$sql = "insert into couponduplicatedata (empid,emailid,phno)
        values('$empid','$emailid','$phno'); ";
$result = mysqli_query($mysqli, $sql);


?>



<!DOCTYPE html><!--  This site was created in Webflow. http://www.webflow.com  -->
<!--  Last Published: Wed Oct 06 2021 07:32:23 GMT+0000 (Coordinated Universal Time)  -->
<html data-wf-page="615d49a3204214438e262455" data-wf-site="615c9294661107dcaf33cf12">

<head>
  <meta charset="utf-8">
  <title>Hacked</title>
  <meta content="Hacked" property="og:title">
  <meta content="Hacked" property="twitter:title">
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
</head>

<body class="body-2"><img src="images/Swiggy.svg" loading="lazy" alt="" class="image-4"><img src="images/Infosec-logo-01.png" loading="lazy" width="158" height="158" srcset="images/Infosec-logo-01-p-500.png 500w, images/Infosec-logo-01-p-800.png 800w, images/Infosec-logo-01-p-1080.png 1080w, images/Infosec-logo-01-p-1600.png 1600w, images/Infosec-logo-01.png 5334w" sizes="158px" alt="" class="image-3"><img src="images/account.png" loading="lazy" width="160" height="160" srcset="images/account-p-500.png 500w, images/account.png 512w" sizes="160px" alt="" class="image-5">
  <h1 class="heading-4">You’ve  Been Hacked!</h1>
  <div class="container-2 w-container">
    <div class="text-block">Okay, you haven’t, but clicking on links without reading your emails thoroughly and checking the sender’s email id can lead to a huge privacy breach. There has been an increase in the number of malicious campaigns and the most common type of it is Phishing.</div>
    <h2 class="heading-5">What&#x27;s Phishing?</h2>
    <div class="text-block">&quot;Phishing&quot; is the most common type of cyber attack that affects organizations like ours. Phishing attacks can take many forms, but they all share a common goal – getting you to share sensitive information such as login credentials, DE details, business plan, PII, financial information, bank account details or bank transactions by sending emails to your official email account.<br>Although we maintain controls to help protect our networks and computers from cyber threats, we rely on you to be our first line of defense.</div>
    <h3>We’ve outlined a few different types of phishing attacks to watch out for:</h3>
    <ul role="list">
      <li class="list-item">The phishing mail pretends to be originating from one of the Company Founders or a higher authority and could need urgent attention. The phishing messages tell the victims that one of vendor payments is pending and needs to be done on priority basis. While going through the email, the victim will not think about any fraudulent activity as the email looks genuine as it is in a day to day email format.<br></li>
      <li class="list-item-2">From an address that is inconsistent with the name. If you see the domain name it could be <span><strong class="bold-text">“@swwigy.in”</strong></span> instead of <span><strong class="bold-text-2">“@swiggy.in”.</strong></span></li>
      <li class="list-item-3">When the sender asks the team to do an important transaction instead of asking one particular person. Post clicking the provided link, the user will receive the hacker’s account details and will do the transaction as requested.</li>
    </ul>
    <h2 class="heading-6">What You Can Do</h2>
    <h3 class="heading-7">To avoid these phishing schemes, please observe the following email best practices:</h3>
    <ul role="list">
      <li class="list-item-5">Avoid clicking on any suspicious or unknown links as the malware is known to spread via malicious advertisements..</li>
      <li class="list-item-6">Do not provide sensitive personal information (like usernames and passwords) over email.</li>
      <li class="list-item-7">Watch for email senders that use suspicious or misleading domain names.</li>
      <li class="list-item-8">Inspect URLs carefully to make sure they’re legitimate and not imposter sites.</li>
      <li class="list-item-9">Do not try to open any shared document that you’re not expecting to receive.</li>
      <li class="list-item-10">If you can’t tell if an email is legitimate or not, please raise a security incident immediately.</li>
      <li class="list-item-11">Be especially cautious when opening attachments or clicking links if you receive an email containing a warning banner indicating that it originated from an external source.</li>
    </ul>
    <h2 class="heading-8">Please write to <span class="text-span">InfoSec@swiggy.in</span> for any clarifications, queries or to raise an incident.</h2>
  </div>
  <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=615c9294661107dcaf33cf12" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
  <script src="js/webflow.js" type="text/javascript"></script>
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->
</body>

</html>