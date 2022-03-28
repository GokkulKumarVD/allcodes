<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stock</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">


    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"> -->
    <!-- Compiled and minified JavaScript -->
    <!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script> -->

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>

    <link rel="stylesheet" href="style.css">

    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>


</head>

<body>
    <?php require 'header.php' ?>

    <a class="btn-floating btn-large cyan pulse tooltipped" id="addd" style="margin-top: 20px; margin-left: 20px;"
    data-position="bottom" data-tooltip="Add device" ><i class="material-icons">add_circle</i></a>

    <a class="btn-floating btn-large cyan pulse tooltipped" id="statistics" style="margin-top: 20px; margin-left: 40px;"
     data-position="bottom" data-tooltip="Stats" ><i class="material-icons">insights</i></a>


    <div class="" id="adddevice" data-aos="zoom-in" data-aos-duration="1000" data-aos-easing="ease-in-out-cubic">
        <div class="container">
            <div class="card center">
                <div class="card-title" style="font-family: 'Bebas Neue', cursive; margin-top: 50px;">
                    <h2 class="center grey-text">ADD DEVICE</h2>
                </div>
                <div class="card-content">
                    <form action="stock.php" method="POST" id="myform">
                        <div class="input-field">
                            <!-- <select id="laptop" name="laptop">
                                <option value="" disabled selected>Choose Laptop</option>
                                <option value="HP">HP</option>
                                <option value="DELL">DELL</option>
                                <option value="LENOVO">Lenovo</option>
                                <option value="MAC">Mac</option>
                            </select> -->
                            <input type="text" name="laptop" id="laptop">
                            <label for="laptop">Laptop brand</label>
                        </div>
                        <div class="input-field">
                            <input type="text" name="price" id="price">
                            <label for="price">Price</label>
                        </div>
                        <div class="input-field">
                            <input type="text" name="lapid" id="lapid">
                            <label for="lapid">Laptop ID</label>
                        </div>
                        <div class="input-field">
                            <button class="btn z-depth-2" id="submitting">Add to stock</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>



    <div class="statics" id="state">
        <div class="container">
            <ul class="collapsible">
                <li>
                    <div class="collapsible-header"><i class="material-icons">laptop_windows</i>Dell</div>
                    <div class="row collapsible-body center">
                        <div class="card col l6">
                            <div class="card-title">
                                Assigned laptops
                            </div>
                            <div class="card-content" id="dell_assigned_loadhere">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                        <div class="card col l6">
                            <div class="card-title">
                                Un-assigned laptops
                            </div>
                            <div class="card-content" id="dell_unassigned_loadhere">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                    </div>
                </li>

                <li>
                    <div class="collapsible-header"><i class="material-icons">laptop_windows</i>Lenovo</div>
                    <div class="row collapsible-body center">
                        <div class="card col l6">
                            <div class="card-title">
                                Assigned laptops
                            </div>
                            <div class="card-content">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                        <div class="card col l6">
                            <div class="card-title">
                                Un-assigned laptops
                            </div>
                            <div class="card-content">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                </li>
                <li>
                    <div class="collapsible-header"><i class="material-icons">laptop_windows</i>HP</div>
                    <div class="row collapsible-body center">
                        <div class="card col l6">
                            <div class="card-title">
                                Assigned laptops
                            </div>
                            <div class="card-content">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                        <div class="card col l6">
                            <div class="card-title">
                                Un-assigned laptops
                            </div>
                            <div class="card-content">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="collapsible-header"><i class="material-icons">laptop_mac</i>Mac</div>
                    <div class="row collapsible-body center">
                        <div class="card col l6">
                            <div class="card-title">
                                Assigned laptops
                            </div>
                            <div class="card-content">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                        <div class="card col l6">
                            <div class="card-title">
                                Un-assigned laptops
                            </div>
                            <div class="card-content">
                                <div><span>Not functional</span></div>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>

    <!-- <div class="laptopstocktable">
        <div class="parallax-container" style="height: 250px;">
            <div class="parallax">
                <img src="img/lappy7.jpg" alt="laptop">
            </div>
        </div>
    </div> -->


    <div class="stock_table" id="stock_id" >
        <div class="card z-depth-2">
            <table class="highlight centered">
                <thead>
                    <tr>
                        <th>UN-ASSIGNED LAPTOP</th>
                        <th>PRICE</th>
                        <th>ID</th>

                    </tr>
                </thead>

                <tbody id="loadhere_laptopid_table">
                    <?php 
                        include 'conn.php';
                        $sql = "select * from addstock where status = 'unassigned' order by id asc ;";

                        //$results = $dbo->query($sql);
                        // mysqli
                        $results = mysqli_query($mysqli, $sql);
                        // Fetch all
                        mysqli_fetch_all($results, MYSQLI_ASSOC);

                        foreach($results as $result){
                            echo"<tr data-aos='zoom-in'><td>$result[laptop_brand]</td><td>$result[price]</td><td>$result[laptop_id]</td></tr>";
                        }
                    ?>
                    <!-- <tr>
                        <td>DELL</td>                   
                        <td>200000</td>
                        <td>SWLP-20000</td>
                    </tr> -->
                    <!-- pushing rows here by jquery -->
                </tbody>
            </table>
        </div>
    </div>
    
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    
    <script>
        AOS.init();
    </script>


    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script>
        $(document).ready(function () {
            $('select').formSelect();

            $('.parallax').parallax();
            $('.tooltipped').tooltip();

            $('#addd').click(function () {
                $('#adddevice').removeClass('adding');
                $('#state').addClass('statics')
            });

            $('#statistics').click(function () {
                $('#state').removeClass('statics');
                $('#adddevice').addClass('adding');
            });

            $('#submitting').click(function (e) {
                e.preventDefault();
                swal({
                    title: "Done!",
                    text: "Successfully added to stock",
                    icon: "success",
                    button: "Aww yiss!",
                });

                var laptop_brand = $('#laptop').val();
                var price = $('#price').val();
                var laptop_id = $('#lapid').val();


                $.get('insert_stock.php', {
                    'laptop_brand': laptop_brand,
                    'price': price,
                    'laptop_id': laptop_id

                }, function () {
                    // $.each(return_data.data, function (key, value) {
                    //     $('#sublob').append("<option>" + value.child + "</option>");
                    //     $('select').formSelect();
                    // });
                }, "json");


                $('#myform')[0].reset();
            });

            $('.collapsible').collapsible();



            $('#statistics').click(function () {

                var laptop_brand = 'dell';
                console.log('worked');
                $.get('stats.php', {
                    'laptop_brand': laptop_brand
                }, function (return_data) {
                    $.each(return_data.data, function (key, value) {
                        $('#dell_assigned_loadhere').empty().append("<div><span>" + value.assigned + " </span></div>");
                        $('#dell_unassigned_loadhere').empty().append("<div><span>" + value.unassigned_laptop + " </span></div>");
                    });

                }, "json");

            });


        });
    </script>

</body>

</html>