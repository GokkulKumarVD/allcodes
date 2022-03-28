<?php


require 'conn.php';


?>


<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT Portal</title>
    <!-- Compiled and minified CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>



    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

    <link rel="stylesheet" href="style.css">
</head>

<body>
    <?php include 'header.php' ?>


    <div class="container center" data-aos="flip-down">
        <div class="card z-depth-3">
            <div class="card-title center" style="font-family: 'Bebas Neue', cursive; margin-top: 50px;">
                <h5 style="font-size: 3rem;">Assign device</h5>
            </div>
            <div class="card-content">
                <form action="index.php" id="myform" method="post" name="registration">

                    <div class="input-field">
                        <a href="#" id="badge"><i class="material-icons prefix">badge</i></a>
                        <input type="text" id="empid" class="empid" name="empid">
                        <label class="subtext" for="empid" style="margin-left: 42px;">Employee ID</label>
                    </div>

                    <div class="input-field">
                        <i class="material-icons prefix" style="color: #039be5">email</i>
                        <input type="email" name="email" id="email" name="email">
                        <label for="email">Employee Email</label>
                    </div>
                    <div class="input-field">
                        <i class="material-icons prefix" style="color: #039be5">thumb_up_alt</i>
                        <input type="email" name="approvedby" id="approvedby" name="approvedby">
                        <label for="approvedby">Approved by (email)</label>
                    </div>
                    <div class="input-field">
                        <i class="material-icons prefix" style="color: #039be5">event_seat</i>
                        <input type="text" name="assignedby" id="assignedby" name="assigned">
                        <label for="assignedby">Assigned by</label>
                    </div>
                    <div class="input-field">
                        <div class="row">
                            <div class="col l1" style="margin-left: -40px;">
                                <a href="#" id="laptop_brand"><i class="material-icons prefix modiicon"
                                        style="color: #039be5">laptop_chromebook</i></a>
                            </div>
                            <div class="col l11 modi">
                                <div class="input-field ">
                                    <select id="laptop" name="laptop">

                                        <option value="" disabled selected>Choose Laptop</option>
                                        <?php
                                        $sql = 'SELECT DISTINCT(laptop_brand) FROM addstock where status="unassigned";';
                                        // $results = $dbo->query($sql);
            
                                        $results = mysqli_query($mysqli, $sql);
                                        // Fetch all
                                        mysqli_fetch_all($results, MYSQLI_ASSOC);
            
                                        foreach ($results as $result) {
                                            echo "<option value=$result[laptop_brand]>$result[laptop_brand]</option>";
                                        }
                                        ?>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>



                    <div class="input-field">
                        <i class="material-icons prefix" style="color: #039be5">confirmation_number</i>
                        <!-- <input type="text" name="laptopid" id="laptopid">
                        <label for="laptopid">Laptop ID</label>  -->
                        <input list="brow" type="text" name="laptopid" id="laptopid" name="laptopid">
                        <datalist id="brow">
                            <!-- <option value="Internet Explorer">
                            <option value="Firefox">
                            <option value="Chrome">
                            <option value="Opera">
                            <option value="Safari"> -->
                        </datalist>
                        <label for="laptopid">Laptop ID</label>
                    </div>

                    <div class="input-field">
                        <button class="btn z-depth-2" id="submit">Assign</button>
                    </div>
                </form>
            </div>
        </div>


    </div>
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>

    <script>
        AOS.init({
            offset: 100,
            delay: 500
        });
    </script>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

    <!-- to send email -->
    <script src="https://smtpjs.com/v3/smtp.js"></script>

    <script>
        $(document).ready(function () {
            $('select').formSelect();





            $('#badge').click(function () {
                var empid = $('#empid').val();


                $.get('darwin_details.php', {
                    'empid': empid
                }, function (return_data) {
                    $.each(return_data.data, function (key, value) {
                        $('#email').val(value.email);
                        $('#approvedby').val(value.reporting_to_email);
                    });
                }, "json");

            });

            $('#laptop_brand').click(function () {
                var laptop = $('#laptop').val();
                $.get('lapidfetch.php', {
                    'laptop_brand': laptop
                }, function (return_data) {
                    $.each(return_data.data, function (key, value) {
                        $('#brow').append("<option value = " + value.laptop_id + ">");
                        console.log(value.laptop_id);
                    });
                }, "json");
            });

            $('#submit').click(function (e) {
                e.preventDefault();
                var empid = $('#empid').val();
                var email = $('#email').val();
                var approvedby = $('#approvedby').val();
                var assignedby = $('#assignedby').val();
                var laptop = $('#laptop').val();
                var laptopid = $('#laptopid').val();
                var assigneddate = new Date().valueOf();


                if ($('#empid').val().length === 0 || $('#email').val().length === 0 || $('#approvedby').val().length === 0 || $('#assignedby').val().length === 0 || $('#laptop').val().length === 0 || $('#laptopid').val().length === 0) {
                    M.toast({
                        html: 'Please fill in all the details'
                        , classes: 'rounded'
                    })
                    return false;
                    exit();
                } else {

                    Email.send({
                        Host: "smtp.gmail.com",
                        Username: "vd.gokkulkumar@swiggy.in",
                        Password: "ibojxfiltxmdxiyg",
                        To: 'senthil.prabhu@swiggy.in',
                        From: "vd.gokkulkumar@swiggy.in",
                        Subject: "Laptop assigned!",
                        Body: `${assignedby} has assigned ${laptop} - ${laptopid} to ${email}. It was approved by ${approvedby}`

                    })


                    $.get('insert_assign.php', {
                        'empid': empid,
                        'email': email,
                        'approvedby': approvedby,
                        'assignedby': assignedby,
                        'laptop': laptop,
                        'assigneddate': assigneddate,
                        'laptopid': laptopid
                    }, function () {
                        // $.each(return_data.data, function (key, value) {
                        //     $('#sublob').append("<option>" + value.child + "</option>");
                        //     $('select').formSelect();
                        // });
                        console.log('worked');
                    }, "json");



                    swal({
                        title: "Done!",
                        text: "Successfully assigned",
                        icon: "success",
                        button: "Aww yiss!",
                    });

                    $('#myform')[0].reset();
                }
            });

        });
    </script>

</body>

</html>