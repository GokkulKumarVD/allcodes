<?php

require "conn.php";

session_start();


$dashname = $_SESSION['username'];
// echo ($dashname);

if (!isset($_SESSION['username'])) {
    header("location: dashlogin.php");
}


?>




<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    <title>Document</title>
</head>

<body>

    <div class="intro py-4 bg-white text-center">
        <div class="container">
            <h1 class="text-primary display-3 my-4">Swiggy infosec quiz</h1>
        </div>
    </div>

    <div class="result py-4 d-none bg-light text-center">
        <div class="container lead">
            <p>Your score <span class="text-center text-primary display-4 p-3">0%</p>
        </div>
    </div>

    <div class="quiz py-4 p-lg-5 bg-primary ">

        <h1 class="my-5 text-white">On with the questions</h1>

        <form class="quiz-form text-light">
            <div class="my-5">
                <p class="lead font-weight-normal">
                    1. What should you do as an employee if you suspect a phishing attack?
                </p>

                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt" value="A">
                    <label class="form-check-label">Open the email and see whether it looks legitimate.</label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt" value="B">
                    <label class="form-check-label">Ignore it. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt" value="C">
                    <label class="form-check-label">Report it to InfoSec@Swiggy.in for investigation. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt" value="D">
                    <label class="form-check-label">Show it to your coworkers to see what they think. </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    2. What are the most common signs of phishing scams?
                </p>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt1" value="A">
                    <label class="form-check-label">Nice graphics and layout </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt1" value="B">
                    <label class="form-check-label">Contains personal information </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt1" value="C">
                    <label class="form-check-label">Unknown sender, sense of urgency, unexpected attachment, or too good to be true </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt1" value="D">
                    <label class="form-check-label">Proper spelling and grammar </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    3. What can happen if you click on a phishing email link or attachment?
                </p>

                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt2" value="A">
                    <label class="form-check-label">The email sender could gain access to company systems. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt2" value="B">
                    <label class="form-check-label">The email sender could steal your personal information or company information. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt2" value="C">
                    <label class="form-check-label">The email sender could distribute malware into the company network. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt2" value="D">
                    <label class="form-check-label">All of above </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    4. Why is it important for me to watch out for phishing emails if my organization has email controls and security in place?
                </p>

                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt3" value="A">
                    <label class="form-check-label">Phishing emails grow more sophisticated all the time. Each one of us needs to be vigilant. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt3" value="B">
                    <label class="form-check-label">IT has several security precautions in place, but they don't control individual users' non-corporate devices. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt3" value="C">
                    <label class="form-check-label">You most likely receive phishing emails on your personal email accounts as well, so it pays to be aware. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt3" value="D">
                    <label class="form-check-label">All of the above </label>
                </div>
            </div>
            

            <div class="my-5">
                <p class="lead font-weight-normal">
                    5. If you’re unsure whether an email is real or a phishing attempt, what should you do? Choose one of the following
                </p>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt4" value="A">
                    <label class="form-check-label">An unknown email sender sounds vague or generic, and is threatening something about one of your online accounts? Report it as phishing. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt4" value="B">
                    <label class="form-check-label">An alert email comes from PayPal or your bank. Open a new browser window and go to your account to see if anything is happening with your account. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt4" value="C">
                    <label class="form-check-label">An offer appears to be from Amazon, but upon closer inspection it's actually from Amzon.co. You should report and delete the email. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt4" value="D">
                    <label class="form-check-label">All of the above </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    6. Identify which among the given is the most secured password. 
                </p>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt5" value="A">
                    <label class="form-check-label">W5@s46t9$ </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt5" value="B">
                    <label class="form-check-label">Abcd1234 </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt5" value="C">
                    <label class="form-check-label">Swiggy123 </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt5" value="D">
                    <label class="form-check-label">2211Rama </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    7. Your business email account has been compromised and leaked in a data breach. What is the best course of action(s)?
                </p>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt6" value="A">
                    <label class="form-check-label">Change your password immediately. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt6" value="B">
                    <label class="form-check-label">Inform the security team of your organization. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt6" value="C">
                    <label class="form-check-label">Change the Password on all sites where you use the same password. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt6" value="D">
                    <label class="form-check-label">All of the above. </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    8. Which of the below channels is handled by Swiggy officially on Social media?
                </p>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt7" value="A">
                    <label class="form-check-label">Twitter Official | We Are Swiggy. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt7" value="B">
                    <label class="form-check-label">Facebook Official | We Are Swiggy.</label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt7" value="C">
                    <label class="form-check-label">Instagram Official | We Are Swiggy. </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt7" value="D">
                    <label class="form-check-label">All the above. </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    9. Users shall not send virus alerts received on email to anyone other than:
                </p>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt8" value="A">
                    <label class="form-check-label">infosec@swiggy.in </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt8" value="B">
                    <label class="form-check-label">swiggy.it@swiggy.in </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt8" value="C">
                    <label class="form-check-label">internalcomms@swiggy.in </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt8" value="D">
                    <label class="form-check-label">Immediate supervisor </label>
                </div>
            </div>

            <div class="my-5">
                <p class="lead font-weight-normal">
                    10. Trying to solve hardware issues by unauthorised support services in external service centres is a breach of BTPL data breach policy?
                </p>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt9" value="A">
                    <label class="form-check-label">True </label>
                </div>
                <div class="form-check my-2 text-white-50">
                    <input type="radio" name="opt9" value="B">
                    <label class="form-check-label">False</label>
                </div>
            </div>

            


            <div class="text-center">
                <input type="submit" class="btn btn-light" value="Submit">
            </div>

        </form>
    </div>

    <script src="script.js">

    </script>

</body>


</html>