<!DOCTYPE html>
<html>
<head>
  <title>Darwin</title>
  <!--Responsive Meta Tag-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <!--Import Google Icon Font-->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <!--Import materialize.css-->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
  
  <!--Import jQuery Library-->
  <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  <!--Import materialize.js-->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
</head>
<body>
<style type="text/css">
	.m20_0{ margin:20px 0px;}
</style>

<nav>
    <div class="nav-wrapper">
        <a href="#" class="brand-logo" style="margin-left: 10px;">IT PORTAL</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="index.php">Assign</a></li>
            <li><a href="search.php">Search</a></li>
            <li><a href="stock.php">Stock</a></li>
            <li><a href="Darwin.php">Darwin</a></li>
        </ul>
    </div>
</nav>


<div class="m20_0">

  
  <!-- Element Showed -->
  <div class="fixed-action-btn" style="bottom: 45px; right: 24px;">
        <a id="menu" class="btn btn-floating btn-large cyan" onclick="$('.tap-target').tapTarget('open')"><i class="material-icons">contact_support</i></a>
   </div>

  <!-- Start Tap Target Structure -->
  <div class="tap-target blue" data-activates="menu">
    <div class="tap-target-content white-text">
      <h5>This table contains Darwin data</h5>
      <p>Please drop an email to it@swiggy.in for further help</p>
    </div>
  </div>
  <!-- End Tap Target Structure -->
</div>
  
<div class="darwin_table" id="darwin_table" >
    <div class="card z-depth-2">
        <table class="highlight centered">
            <thead>
                <tr>
                    <th>EMPID</th>
                    <th>EMAIL</th>
                    <th>GRADE</th>
                    <th>REPORTING TO</th>
                    <th>WORK LOCATION</th>
                    <th>JOINED DATE</th>
                </tr>
            </thead>

            <tbody id="loadhere_laptopid_table" >
                <?php 
                    include 'conn.php';
                    $sql = "select * from Darwin;";

                    //$results = $dbo->query($sql);
                    // mysqli
                    $results = mysqli_query($mysqli, $sql);
                    // Fetch all
                    mysqli_fetch_all($results, MYSQLI_ASSOC);

                    foreach($results as $result){
                        echo"<tr data-aos='zoom-in'><td>$result[empid]</td><td>$result[email]</td><td>$result[grade]</td><td>$result[reporting_to_email]</td><td>$result[work_location]</td><td>$result[joined_date]</td></tr>";
                    }
                ?>
                <!-- <tr>
                    <td>1111</td>                   
                    <td>G@G.COM</td>
                    <td>5</td>
                    <td>G@G.COM</td>
                    <td>MC</td>
                    <td>21-06-21</td>
                </tr> -->
                <!-- pushing rows here by jquery -->
            </tbody>
        </table>
    </div>
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script>
        AOS.init();
    </script>
</div>




</body>
</html>