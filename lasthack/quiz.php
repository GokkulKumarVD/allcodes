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
    $_SESSION['empid'] = $emailid;



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
<!DOCTYPE html>
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
  <link href="images/swiggy-1.svg" rel="shortcut icon" type="image/x-icon">
  <link href="images/swiggy-1.svg" rel="apple-touch-icon">
 
</head>

<body class="body-2">

  
<form class="quiz-form" id="quizSubmit" >
    <div>
      <div class="container-5 w-container"><img src="images/image-1-1.png" loading="lazy" width="143" alt="" class="image-4"><img src="images/Infosec-logo-01.png" loading="lazy" width="100" sizes="100px" srcset="images/Infosec-logo-01-p-500.png 500w, images/Infosec-logo-01-p-800.png 800w, images/Infosec-logo-01-p-1080.png 1080w, images/Infosec-logo-01-p-1600.png 1600w, images/Infosec-logo-01.png 5334w" alt="" class="image-5"></div>
      <div class="container-6 w-container">
      <div class="result scorecard py-4 d-none bg-light text-center">
            <div class="container lead scorecard-body">
              <h4>Your score <span class="text-center text-primary display-4 p-3">0%</h4>
            </div>
            <div class="stopwatch">Time left : <span id="timer"></span></div>
          </div>
        <div class="div-block-2">
          <!-- <form action="" method="post"> -->
            <h4 class="heading-6">1. The ____________ Domain Name Server data will spread to the ISPs & will be cached there.</h4>
            <div class="w-form">
              <label class="w-radio">
                <input type="radio" data-name="Radio" id="radio" name="opt" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Working.</span></label>
              <label class="w-radio">
                <input type="radio" data-name="Radio" id="radio-2" name="opt" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Compromised.</span>
              </label>
              <label class="w-radio">
                <input type="radio" data-name="Radio" id="radio-3" name="opt" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Corrupted.</span>
              </label>
              <label class="w-radio"><input type="radio" data-name="Radio" id="radio-4" name="opt" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-4" class="w-form-label">Poisoned.</span>
              </label>
            </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-7">2. Users could be influenced by DNS hijacking if the government of that country uses DNS redirecting as a mechanism to mask censorship.</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 5" id="radio-5" name="opt1" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">True.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 6" id="radio-6" name="opt1" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">False.</span>
            </label>
            <!-- <label class="w-radio">
              <input type="radio" data-name="Radio 7" id="radio-7" name="opt1" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Unknown sender, sense of urgency, unexpected attachment, or too good to be true.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 8" id="radio-8" name="opt1" value="D" class="w-form-formradioinput w-radio-input">
              <span for="radio-8" class="w-form-label">Proper spelling and grammar.</span>
            </label> -->

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-5">3. Developing a fake or not so useful website that is meant to just fetch the IP address can be easily done by attackers.</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 9" id="radio-9" name="opt2" value="A" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label">True.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 10" id="radio-10" name="opt2" value="B" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label">False.</span>
            </label>
            <!-- <label class="w-radio">
              <input type="radio" data-name="Radio 11" id="radio-11" name="opt2" value="C" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label">The
                email sender could distribute malware into the company network.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 12" id="radio-12" name="opt2" value="D" class="w-form-formradioinput w-radio-input">
              <span for="radio-12" class="w-form-label">All of the
                above.</span>
            </label> -->

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-4">4. _________ is the practice and precaution taken to protect valuable information from unauthorised access, recording disclosure or destruction.</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 13" id="radio-13" name="opt3" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label"> Information Security.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 14" id="radio-14" name="opt3" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Network Security.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 15" id="radio-15" name="opt3" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Physical Security.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 16" id="radio-16" name="opt3" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-16" class="w-form-label">Database Security.</span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-8">5. How do I stop DNS tunnelling attacks?.</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 17" id="radio-17" name="opt4" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Staying vigilant for suspicious domains.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 18" id="radio-18" name="opt4" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Reporting suspicious domains to the InfoSec team.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 19" id="radio-19" name="opt4" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Reporting suspicious domains to threat intelligence platforms.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 20" id="radio-20" name="opt4" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-20" class="w-form-label">All of the above.</span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-9">6. Employees are individually liable for all damages incurred as a result of violating Swiggy security policy, copyright, and licensing agreements.</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 21" id="radio-21" name="opt5" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label"><strong class="bold-text-2">True.</strong></span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 22" id="radio-22" name="opt5" value="B" class="w-form-formradioinput w-radio-input"><span class="radio-button-label w-form-label">False.</span>
            </label>
            <!-- <label class="w-radio">
              <input type="radio" data-name="Radio 23" id="radio-23" name="opt5" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Swiggy123</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 24" id="radio-24" name="opt5" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-24" class="radio-button-label-2 w-form-label">2211Rama</span>
            </label> -->

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-10">7. How does one prevent a brute force attack?</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 25" id="radio-25" name="opt6" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label"><strong><em class="italic-text">Setting a lengthy password.</em></strong></span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 26" id="radio-26" name="opt6" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Increase password complexity.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 27" id="radio-27" name="opt6" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">Set limits on login failures.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 28" id="radio-28" name="opt6" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-28" class="w-form-label"><strong class="bold-text">All of the above.</strong></span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h4 class="heading-11"><strong>8. </strong>Which month is celebrated as InfoSec & CyberSecurity awareness month worldwide?</h4>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 29" id="radio-29" name="opt7" value="A" class="w-form-formradioinput w-radio-input">
              <span class="w-form-label"><strong><em class="italic-text">October.</em></strong></span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 30" id="radio-30" name="opt7" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">August.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 31" id="radio-31" name="opt7" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">April.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 32" id="radio-32" name="opt7" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-32" class="w-form-label"><strong class="bold-text">November.</strong></span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h3 class="heading-12"><strong class="bold-text-4">9. What are the advantages of cyber security?
          </strong></h3>
          <div class="w-form">
            <label class="w-radio">
              <input type="radio" data-name="Radio 33" id="radio-33" name="opt8" value="A" class="w-form-formradioinput w-radio-input"><span class="w-form-label">
                It protects the business against ransomware, malware, social engineering, and phishing.
              </span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 34" id="radio-34" name="opt8" value="B" class="w-form-formradioinput w-radio-input"><span class="w-form-label">It protects end-users.</span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 35" id="radio-35" name="opt8" value="C" class="w-form-formradioinput w-radio-input"><span class="w-form-label">
                It gives good protection for both data as well as networks.
              </span>
            </label>
            <label class="w-radio">
              <input type="radio" data-name="Radio 36" id="radio-36" name="opt8" value="D" class="w-form-formradioinput w-radio-input"><span for="radio-36" class="w-form-label"><strong class="bold-text">Increase recovery time after a breach.</strong></span>
            </label>

          </div>
        </div>
        <div class="div-block-2">
          <h3><strong class="bold-text-5">10. Any kind of threat that compromises computer systems, resulting in data loss and security breach of the company is called an Accident.</strong></h3>
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

     <script type="text/javascript">
    ! function(o, c) {
      var n = c.documentElement,
        t = " w-mod-";
      n.className += t + "js", ("ontouchstart" in o || o.DocumentTouch && c instanceof DocumentTouch) && (n.className += t + "touch")
    }(window, document);
    document.getElementById('timer').innerHTML = 05 + ":" + 00;
startTimer();
 function startTimer() {
  var presentTime = document.getElementById('timer').innerHTML;
  var timeArray = presentTime.split(/[:]+/);
  var m = timeArray[0];
  var s = checkSecond((timeArray[1] - 1));
  if(s==59){m=m-1}
  if(m<0){
    document.getElementById("quizSubmit").submit.click();
    return
  }
  
  document.getElementById('timer').innerHTML =
    m + ":" + s;
  // console.log(m)
  setTimeout(startTimer, 1000);
  
}

function checkSecond(sec) {
  if (sec < 10 && sec >= 0) {sec = "0" + sec}; // add zero in front of numbers < 10
  if (sec < 0) {sec = "59"};
  return sec;
}
  </script>
  <script>
    let correctAnswer = ['D', 'A', 'A', 'A', 'D', 'A', 'D', 'A', 'A', 'B'];
    console.log('working')
    let form = document.querySelector('.quiz-form');
    let result = document.querySelector('.result');

  //   var presentTime = document.getElementById('timer').innerHTML;
  // var timeArray = presentTime.split(/[:]+/);
  // let min = parseInt(timeArray[0]);
  // let sec =parseInt(timeArray[0]);
  // let testTime = 3;
  // let timeTaken = testTime * 60 - min * 60 - sec;
  // console.log("timeTaken",timeTaken);

    form.addEventListener('submit', (e) => {
      console.log("submitted")
      e.preventDefault();
      result.style.display = 'block';
      var presentTime = document.getElementById('timer').innerHTML;
  var timeArray = presentTime.split(/[:]+/);
  let min = parseInt(timeArray[0]);
  let sec =parseInt(timeArray[1]);
  let testTime = 5;
  let timeTaken = testTime * 60 - min * 60 - sec;
  // console.log("timeTaken",timeTaken);

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
        console.log("timeTaken",timeTaken);
        localStorage.setItem("timeTaken", timeTaken);
        if (emailid === null ||
          emailid === undefined) {
          alert('Enter all the fields');
        } else {
          $.get('insertscore.php', {
            'emailid': emailid,
            'score': score,
            'starttime': starttime,
            'timetaken':timeTaken
          }, function() {
            console.log('worked');

          }, "json");

        }

      });

      window.setTimeout(function() {
        // window.location.href = "http://www.infoquiz.swiggy.in/";
        window.location.href = "http://localhost/quizapp/completion.php";
      }, 3000);

    });

  </script>



  </div>
  </div>


  <!-- <script src="script.js"></script> -->






</body>

</html>