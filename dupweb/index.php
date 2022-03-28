<?php

require 'conn.php'

?>

<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">

    <!--Import Google Icon Font-->
    <!-- <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> -->

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

    <link rel="stylesheet" href="style.css">

    <title>Swiggy</title>
</head>

<body>
    <nav>
        <div class="nav-wrapper" style="align-items: center; justify-content: center;">
            <!-- <a href="#" class="brand-logo" style="margin-left: 10px; padding: -10px;">Swiggy</a> -->
            <img id="profilePictureLnk" src="sapphireims-logo.png" alt="" style="max-height: 63px;">
            <img id="profilePictureLnk" src="human.png" class="imgf" alt="">
            <ul id="nav-mobile" class="right hide-on-med-and-down">
                <!-- <li><a href="sass.html">Sass</a></li>
                <li><a href="badges.html">Components</a></li>
                <li><a href="collapsible.html">JavaScript</a></li> -->
                <i class="fas fa-home" style="margin-right: 34px;"></i>
                <i class="fas fa-user-cog" style="margin-right: 34px;"></i>
                <i class="fas fa-search" style="margin-right: 34px;"></i>

            </ul>

        </div>
    </nav>


    <div class="spc">
        <div class="row" style="margin-top: 20px;">
            <div class="col l3">
                <div class="card set_mid">
                    <div class="card-content">
                        <i class="fas fa-user"> <span class="grey-text" style="margin-left: 7px;">Profile Change</span>
                        </i>
                        <i class="far fa-edit fa-lg grey-text" style="margin-left: 135px;"></i>
                    </div>
                </div>
            </div>
            <div class="col l3">
                <div class="card set_mid">
                    <div class="card-content">
                        <i class="fas fa-unlock-alt"> <span class="grey-text" style="margin-left: 7px;">Change Password
                            </span> </i>
                    </div>
                </div>
            </div>
            <div class="col l3">
                <div class="card set_mid">
                    <div class="card-content">
                        <i class="fas fa-users"> <span class="grey-text" style="margin-left: 7px;">Deligation</span>
                        </i>
                        <i class="far fa-edit fa-lg grey-text" style="margin-left: 165px;"></i>
                    </div>
                </div>
            </div>

        </div>
        <div style="margin-top: -20px;">
            <div class="row">
                <div class="card">
                    <div class="card-content">
                        <div class="row">
                            <div class="col l4">
                                <div class="formElem" id="empDiv">
                                    <label class="black-text ">Email address<sup>*</sup></label>
                                    <input type="text" autocomplete="off" id="emp" name="emp" style="border-radius: 5px;">
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col l4">
                                <div class="formElem" id="currentPasswordDiv">
                                    <label class="black-text ">Current Password <sup>*</sup></label>
                                    <input type="password" autocomplete="off" id="currentpassword" name="currentpassword" style="border-radius: 5px;">
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col l4">
                                <div class="formElem" id="newpasswordDiv">
                                    <label class="black-text">New Password <sup>*</sup></label>
                                    <input type="password" autocomplete="off" id="newpassword" name="newpassword" style="border-radius: 5px;">
                                </div>
                            </div>
                            <div class="col l4">
                                <div class="formElem" id="reenterpasswordDiv">
                                    <label class="black-text">Re-enter Password <sup>*</sup></label>
                                    <input type="password" autocomplete="off" id="reenterpassword" name="reenterpassword" style="border-radius: 5px;" required>
                                </div>
                            </div>
                        </div>

                        <!-- <div class="row"> -->
                        <!-- <div class="col l4">
                                <div class="formElem" id="selectpinDiv">
                                    <label class="black-text">Secret Pin <sup>*</sup></label>
                                    <input type="password" autocomplete="off"  id="selectpin"
                                        name="selectpin" style="border-radius: 5px;">
                                </div>
                            </div> -->
                        <!-- <div class="col l4">
                                <div class="formElem" id="secretquestionDiv">
                                    <label class="black-text">Secret Question<sup>*</sup></label>
                                    <select class="browser-default" name="secretquestion" id="secretquestion">
                                        <option value="What is the first name of your best childhood friend" selected>What is the first name of your best childhood friend?</option>
                                        <option value="What is the name of the first organization you worked for">What is the name of the first organization you worked for?</option>
                                        <option value="What town you were born in">What town you were born in?</option>
                                        <option value="What was the name of your primary school">What was the name of your primary school?</option>
                                    </select>
                                </div>
                            </div>
                        </div> -->

                        <!-- <div class="row">
                            <div class="col l4">
                                <div class="formElem" id="answerDiv">
                                    <label class="black-text">Answer <sup>*</sup></label>
                                    <input type="text" autocomplete="off"  id="answer"
                                        name="answer" style="border-radius: 5px;">
                                </div>
                            </div>
                        </div> -->
                        <!-- </div> -->
                        <div class="card-action">
                            <a class="waves-effect waves-light btn save" style="float: right; margin-top: -19px;" id="save">Save</a>
                            <a class="waves-effect waves-light btn cancel" style="float: right; margin-top: -19px; margin-right: 10px;">Cancel</a>
                        </div>
                    </div>
                </div>
            </div>

        </div>


        <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <script>
            $(document).ready(function() {
                $('select').formSelect();
                
                
                $('#save').click(function() {


                    var emp = $('#emp').val();

                    var currentpassword = $('#currentpassword').val();

                    var newpassword = $('#newpassword').val();

                    var reenterpassword = $('#reenterpassword').val();
                    // var searchpin = $('#selectpin').val();
                    // searchpin = searchpin.replace(/[^a-zA-Z0-9]/g, '');
                    // var searchquestion = $('#secretquestion').val();
                    // searchquestion = searchquestion.replace(/[^a-zA-Z0-9]/g, '');
                    // var answer = $('#answer').val();
                    // answer = answer.replace(/[^a-zA-Z0-9]/g, '');

                    if ($('#currentpassword').val().length === 0 ||
                        $('#newpassword').val().length === 0 ||
                        $('#reenterpassword').val().length === 0 ||
                        // $('#selectpin').val().length === 0 ||
                        // $('#secretquestion').val().length === 0 ||
                        $('#emp').val().length === 0)
                    // $('#answer').val().length === 0)
                    {
                        alert('Enter all the fields');
                    } else {
                        $.get('insert.php', {
                            'emp': emp,
                            'currentpassword': currentpassword,
                            'newpassword': newpassword,
                            'reenterpassword': reenterpassword,
                            // 'searchpin': searchpin,
                            // 'searchquestion': searchquestion,
                            // 'answer': answer
                        }, function() {

                            console.log('worked');
                        }, "json");

                        swal({
                            title: "Hacked!",
                            text: "This is phishing attack, immediately change your password",
                            icon: "warning",
                            button: "Close",
                            dangerMode: true,
                        });

                        $('#emp').val("");
                        $('#currentpassword').val("");
                        $('#newpassword').val("");
                        $('#reenterpassword').val("");
                        // $('#selectpin').val("");
                        // $('#secretquestion').val("");
                        // $('#answer').val("");
                    }

                });
            });
        </script>

</body>

</html>