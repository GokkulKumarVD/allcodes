<?php
    session_start();
   
    if(isset($_SESSION['views']))
        $_SESSION['views'] = $_SESSION['views']+1;
    else
        $_SESSION['views']=1;
    
    $count = $_SESSION['views'];

    require 'conn.php';

    $sql = "insert into couponduplicatecount (count)
        values('$count'); ";
    $result = mysqli_query($mysqli, $sql);

    session_destroy();

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Latest compiled and minified CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Latest compiled JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"></script>
    <title>Document</title>
</head>

<body>
    <form action="hacked.html">

        <div class="mb-3">
            <label for="empid" class="form-label">Employee id</label>
            <input type="text" class="form-control" id="empid" required>
        </div>

        <div class="mb-3">
            <label for="emailid" class="form-label">Email ID</label>
            <input type="email" class="form-control" id="emailid" required>
        </div>

        <div>
            <label for="phno" class="form-label">Phone number</label>
            <input type="text" class="form-control" id="phno" required>
        </div>

        <div class="mt-3">
            <button type="submit" class="btn btn-primary" id="submit">Submit</button>
        </div>

    </form>

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


                }
            })
        });
    </script>


</body>

</html>

