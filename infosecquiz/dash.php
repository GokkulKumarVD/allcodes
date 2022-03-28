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

    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">

    <!--Import Google Icon Font-->
    <!-- <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> -->

    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

    <link rel="stylesheet" href="btnstyle.css">

    <title>Dashboard</title>
</head>

<body>
    <nav>
        <div class="nav-wrapper">
            <a href="#" class="brand-logo" style="margin-left: 65px;">Victim's data</a>
            <ul id="nav-mobile" class="right hide-on-med-and-down">
                <!-- <li><a href="sass.html">Sass</a></li>
                <li><a href="badges.html">Components</a></li> -->
                <form method="post" action="logout.php">
                    <li><input class="waves-effect waves-light btn " type="submit" value="logout"> </li>
                </form>

            </ul>
        </div>
    </nav>
    <div class="continerdash">
        <div class="row ">
            <div class="col l4 ">
                <div class="card">
                    <div class="card-content valign center">
                        <h3 class="grey-text" id="button" style="cursor: pointer;">Number of entries</h3>
                    </div>
                    <hr>
                    <div class="card-content center">

                        <?php
                        $sql = 'SELECT count(empid) as cnt FROM infoquizlogin;';
                        // $results = $dbo->query($sql);

                        $results = mysqli_query($mysqli, $sql);
                        // Fetch all
                        mysqli_fetch_all($results, MYSQLI_ASSOC);

                        foreach ($results as $result) {
                            echo "<h2 class='grey-text'>$result[cnt]</h2>";
                        }
                        ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-content">
            <table class="highlight centered">
                <thead>
                    <tr>
                        <th>Email ID</th>
                        <th>Score</th>
                        <th>Start Time</th>
                        <th>End Time</th>
                        <th>Total seconds taken</th>
                    </tr>
                </thead>

                <tbody>

                    <?php
                    $sql = 'SELECT emailid,score,starttime,endtime,timetaken FROM infoquizlogin;';
                    // $results = $dbo->query($sql);

                    $results = mysqli_query($mysqli, $sql);
                    // Fetch all
                    mysqli_fetch_all($results, MYSQLI_ASSOC);

                    foreach ($results as $result) {
                        echo "<tr><td>$result[emailid]</td><td>$result[score]</td><td>$result[starttime]</td><td>$result[endtime]</td><td>$result[timetaken]</td></tr>";
                    }
                    ?>

                </tbody>
            </table>
        </div>

    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script>
        $('#button').click(function() {
            window.location.href = 'dum.php';
        })
    </script>

</body>

</html>