<?php

require "conn.php";

session_start();

$empid = $_SESSION['empid'];
$emailid = $_SESSION['emailid'];
$starttime = $_SERVER['REQUEST_TIME'];



if (!isset($_SESSION['empid'])) {
  // echo('not set');
  header("location: index.php");
}

$session_value = (isset($_SESSION['emailid'])) ? $_SESSION['emailid'] : '';

if (isset($_POST['submit'])) {
  $empid = $_POST['empid'];
  $emailid = $_POST['emailid'];

  $_SESSION['empid'] = $empid;
  $_SESSION['emailid'] = $emailid;



  if (!empty($empid) & !empty($emailid)) {
    $sql = "select * from infoquizlogin where emailid=$emailid";
    $result = mysqli_query($mysqli, $sql);
    if (mysqli_num_rows($result) == 0) {
      $sql = "insert into infoquizlogin (empid, emailid) values('$empid','$emailid'); ";
      $result = mysqli_query($mysqli, $sql);
      header("location:quiz.php");
    } else {
      header("location:alreadytaken.php");
    }

    // header("location:quiz.php");
  }
}


?>



<!DOCTYPE html><!--  This site was created in Webflow. http://www.webflow.com  -->
<!--  Last Published: Thu Oct 07 2021 13:53:52 GMT+0000 (Coordinated Universal Time)  -->
<html data-wf-page="615edadc00709b67481cbfac" data-wf-site="615ed1d6c2f57d1e0c0717d6">

<head>
  <meta charset="utf-8">
  <title>quiz</title>
  <meta content="quiz" property="og:title">
  <meta content="quiz" property="twitter:title">
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

<body class="body-2">

  <form class="quiz-form">
    <div>
      <div class="container-5 w-container"><img src="images/image-1-1.png" loading="lazy" width="143" alt="" class="image-4"><img src="images/Infosec-logo-01.png" loading="lazy" width="100" sizes="100px" srcset="images/Infosec-logo-01-p-500.png 500w, images/Infosec-logo-01-p-800.png 800w, images/Infosec-logo-01-p-1080.png 1080w, images/Infosec-logo-01-p-1600.png 1600w, images/Infosec-logo-01.png 5334w" alt="" class="image-5"></div>
      <div class="container-6 w-container">
        <div class="div-block-2">
          <div class="result py-4 d-none bg-light text-center">
            <div class="container lead">
              <p>Your score <span class="text-center text-primary display-4 p-3">0%</p>
            </div>
          </div>
          <form action="" method="post">
            <h4 class="heading-6">1. As an employee what would you do if you suspect a phishing attack?</h4>
            <div class="w-form">
              <label class="w-radio">
                <input type="radio" data-name="Radio" id="radio" name="opt" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Open the email and check whether it
                  looks legitimate.</span></label>
              <label class="w-radio">
                <input type="radio" data-name="Radio" id="radio-2" name="opt" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Ignore it.</span>
              </label>
              <label class="w-radio">
                <input type="radio" data-name="Radio" id="radio-3" name="opt" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Report it to InfoSec@Swiggy.in for investigation.</span>
              </label>
              <label class="w-radio"><input type="radio" data-name="Radio" id="radio-4" name="opt" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-4" class="w-form-label">Show it to your
                  coworkers to see what they think.</span>
              </label>
            </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-7">2. What are the most common signs of phishing scams?</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 5" id="radio-5" name="opt1" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Nice graphics and layout.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 6" id="radio-6" name="opt1" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Contains personal
                information.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 7" id="radio-7" name="opt1" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Unknown sender, sense of urgency, unexpected attachment, or too good to be true.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 8" id="radio-8" name="opt1" value="D" class="w-form-formradioinput w-radio-input">
              <span for="radio-8" class="w-form-label">Proper spelling and grammar.</span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-5">3. What can happen if you click on a phishing email link or attachment?</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 9" id="radio-9" name="opt2" value="A" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label">The email sender could gain access
                to company systems.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 10" id="radio-10" name="opt2" value="B" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label">The email sender could steal your personal information or company
                information.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 11" id="radio-11" name="opt2" value="C" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label">The
                email sender could distribute malware into the company network.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 12" id="radio-12" name="opt2" value="D" class="w-form-formradioinput w-radio-input">
              <span for="radio-12" class="w-form-label">All of the
                above.</span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-4">4. Why is it important for you to watch out for phishing emails if your organization has
            email controls and security in place?</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 13" id="radio-13" name="opt3" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Phishing emails grow more
                sophisticated all the time. Each one of us needs to be vigilant.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 14" id="radio-14" name="opt3" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">IT has several security precautions
                in place, but they don&#x27;t control individual users&#x27; non-corporate devices.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 15" id="radio-15" name="opt3" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">You most likely receive phishing
                emails on your personal email accounts as well, so it pays to be aware.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 16" id="radio-16" name="opt3" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-16" class="w-form-label">All of the
                above.</span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-8">5. If you’re unsure whether an email is real or a phishing attempt, what should you do?
            Choose one of the following.</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 17" id="radio-17" name="opt4" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">An unknown email sender sounds
                vague or generic, and is threatening you about one of your online accounts. Report it as
                phishing.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 18" id="radio-18" name="opt4" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">An
                alert email comes from PayPal or your bank. Open a new browser window and go to your account to see if
                anything is happening with your account.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 19" id="radio-19" name="opt4" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">An offer appears to be from Amazon,
                but upon closer inspection it&#x27;s actually from Amzon.co. You should report and delete the
                email.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 20" id="radio-20" name="opt4" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-20" class="w-form-label">All of the above.</span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-9">6. Identify which among the given is the most secured password.</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 21" id="radio-21" name="opt5" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label"><strong class="bold-text-2">W5@s46t9$</strong></span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 22" id="radio-22" name="opt5" value="B" class="w-form-formradioinput w-radio-input"><span class="radio-button-label w-form-label">Abcd1234</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 23" id="radio-23" name="opt5" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Swiggy123</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 24" id="radio-24" name="opt5" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-24" class="radio-button-label-2 w-form-label">2211Rama</span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-10">7. Your business email account has been compromised and leaked in a data breach. What is
            the best course of action(s)?</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 25" id="radio-25" name="opt6" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label"><strong><em class="italic-text">Change your password immediately.</em></strong></span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 26" id="radio-26" name="opt6" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Inform the security team of your
                organization.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 27" id="radio-27" name="opt6" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Change
                the Password on all sites where you use the same password.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 28" id="radio-28" name="opt6" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-28" class="w-form-label"><strong class="bold-text">All of the above.</strong></span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-11"><strong>8. </strong>Which of the below channels is handled by Swiggy officially on Social
            media?</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 29" id="radio-29" name="opt7" value="A" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label"><strong><em class="italic-text">Twitter Official | We Are Swiggy.</em></strong></span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 30" id="radio-30" name="opt7" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Facebook Official | We Are
                Swiggy.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 31" id="radio-31" name="opt7" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Instagram Official | We Are Swiggy.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 32" id="radio-32" name="opt7" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-32" class="w-form-label"><strong class="bold-text">All of the above.</strong></span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h3 class="heading-12"><strong class="bold-text-4">9. Users shall not send virus alerts received on email to
              anyone other than:</strong></h3>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 33" id="radio-33" name="opt8" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">
                infosec@swiggy.in
              </span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 34" id="radio-34" name="opt8" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">swiggy.it@swiggy.in</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 35" id="radio-35" name="opt8" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">
                internalcomms@swiggy.in
              </span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 36" id="radio-36" name="opt8" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-36" class="w-form-label"><strong class="bold-text">Immediate supervisor</strong></span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h3><strong class="bold-text-5">10. Trying to solve hardware issues by unauthorized support services in external
              service centers is a breach of BTPL data breach policy?</strong></h3>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 37" id="radio-37" name="opt9" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">True</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 38" id="radio-38" name="opt9" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">False</span>
            </label>

          </div>
        </div>
        <!-- <a href="#" class="button w-button" id="submit" name="submit">Submit</a> -->
        <input type="submit" class="button w-button" value="Submit" id="submit" name="submit">
      </div>
  </form>
  <!-- <script src="https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=615ed1d6c2f57d1e0c0717d6" type="text/javascript" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script> -->
  <!-- <script src="js/webflow.js" type="text/javascript"></script> -->
  <!-- [if lte IE 9]><script src="https://cdnjs.cloudflare.com/ajax/libs/placeholders/3.0.2/placeholders.min.js"></script><![endif] -->

  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>

  <script>
    let correctAnswer = ['C', 'C', 'D', 'D', 'D', 'A', 'D', 'D', 'A', 'A'];
    console.log('working')
    let form = document.querySelector('.quiz-form');
    let result = document.querySelector('.result');

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      result.style.display = 'block';

      let score = 0;

      let userAnswer = [form.opt.value,
        form.opt1.value, form.opt2.value, form.opt3.value, form.opt4.value, form.opt5.value, form.opt6.value, form.opt7.value,
        form.opt8.value, form.opt9.value
      ];
      console.log(userAnswer)

      userAnswer.forEach((element, index) => {
        if (element === correctAnswer[index]) {
          score += 1;
        }
      });
      console.log(score);

      scrollTo(0, 0);
      result.classList.remove('d-none');

      let output = 0;
      let tm = setInterval(() => {
        result.querySelector('span').textContent = `${output}/10`;
        if (output === score) {
          clearInterval(tm);
        } else {
          output++;
        }

      }, 100)



      // ----------------------------------------------------------------

      var emailid = '<?php echo $session_value; ?>';
      var starttime = '<?php echo $starttime; ?>';
      console.log(emailid);
      console.log(starttime);




      $(function() {
        console.log(emailid);
        console.log(score);
        if (emailid === null ||
          emailid === undefined) {
          alert('Enter all the fields');
        } else {
          $.get('insertscore.php', {
            'emailid': emailid,
            'score': score,
            'starttime': starttime
          }, function() {
            console.log('worked');

          }, "json");

        }

      });

      window.setTimeout(function() {
        window.location.href = "http://www.infoquiz.swiggy.in/";
      }, 3000);

    });
  </script>



  </div>
  </div>


  <!-- <script src="script.js"></script> -->






</body>

</html>