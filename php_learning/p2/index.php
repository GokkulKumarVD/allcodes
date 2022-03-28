<?php
    require 'conn.php';

?>


<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <style>
        .error {
            outline: 1px dashed red !important;
        }
    </style>
</head>

<body>
    <nav>
        <div class="nav-wrapper">
            <!-- <a href="#" class="brand-logo">Swiggy</a> -->
            <!-- <ul id="nav-mobile" class="right hide-on-med-and-down">
            <li><a href="#">Dummy</a></li>
            <li><a href="#">Dummy</a></li>
            <li><a href="#">Dummy</a></li>
          </ul> -->
        </div>
    </nav>

    <div class="container">
        <div class="row center">
            <div class="col l6">
                <div class="card z-depth-2">
                    <div class="card-content">
                        <form action="">
                            <div class="input-field">
                                <input type="text" name="orderid" id="orderid" >
                                <label class="subtext" for="orderid">Order ID</label>
                            </div>
                            <div class="input-field">
                                <input type="text" name="ordervalue" id="ordervalue">
                                <label class="subtext" for="ordervalue">Order Value</label>
                            </div>
                            <div class="input-field">
                                <input type="text" name="phonenum" id="phonenum">
                                <label class="subtext" for="phonenum">Phone number</label>
                            </div>
                            <div class="input-field">
                                <select name="lob" id="lob">
                                    <option value="" disabled selected>Choose LOB</option>
                                    <?php
                                        $sql = "select distinct prt from table1";
                                        $results = $dbo->query($sql);
                                
                                    
                                    foreach($results as $row) { 
                                      echo  "<option value=$row[prt]>$row[prt]</option>";
                                    }
                                    ?>
                                </select>
                            </div>
                            <div class="input-field">
                                <select name="segment" id="segment">
                                    <option value="" disabled selected>CX segment</option>
                                    <option value="High">High</option>
                                    <option value="Medium">Medium</option>
                                    <option value="Low">Low</option>
                                    <option value="New">New</option>
                                </select>
                            </div>

                            <div class="input-field">
                                <select name="sublob" id="sublob">
                                    <option value="" disabled>Choose sub LOB</option>
                                </select>
                            </div>

                            <div class="input-field">
                                <button type="submit" class="btn z-depth-2" id="sub"> Submit </button>
                                <button type="submit" class="btn z-depth-2" id="clear"> Clear </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div class="col l6">
                <div class="card z-depth-2">
                    <table class="highlight centered">
                        <thead>
                            <tr>
                                <th>ORDER ID</th>
                                <th>PHONE NUMBER</th>
                                <th>RESULT</th>
                            </tr>
                        </thead>

                        <tbody id="loadhere">
                            <?php
                                $sql = "select order_id, phone_number, calculated_result from table3 order by id desc";
                                $results = $dbo->query($sql);
                        
                            
                                foreach($results as $row) { 
                                    echo  "<tr><td>$row[order_id]</td><td>$row[phone_number]</td><td>$row[calculated_result]</td></tr>";
                                }
                            ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

    <script>
        $(document).ready(function () {
            $('select').formSelect();

            // check if values are there
            $(function () {
                $('#sub').click(function (e) {
                    e.preventDefault()
                    $('#orderid').removeClass("error");
                    var txt = $('#orderid');
                    if (txt.val() != null && txt.val() != '') {
                        $('#sub').click(function (e) {
                            // e.preventDefault();
                            var orderid = $('#orderid').val();
                            var ordervalue = $('#ordervalue').val();
                            var phonenum = $('#phonenum').val();
                            var lob = $('#lob').val();
                            var segment = $('#segment').val();
                            var child = $('#sublob').val()

                            $.get('datatable.php', {
                                'orderid': orderid,
                                'ordervalue': ordervalue,
                                'phonenum': phonenum,
                                'lob': lob,
                                'segment': segment,
                                'child': child
                            }, function (return_data) {
                                $.each(return_data.data, function (key, value) {
                                    $("#loadhere").prepend("<tr><td>" + value.order_id + "</td><td>" + value.phone_number + "</td><td>" + value.calculated_result + "</td></tr>")
                                    // console.log("<td>" +value.order_id + "</td><td>"+value.phone_number+"</td><td>"+value.calculated_result+"</td>")
                                });
                            }, "json");
                        });
                    } else {
                        $('#orderid').addClass("error");
                    }
                })
            });



            // cat change
            $('#lob').change(function () {
                var lob = $('#lob').val();
                $('#sublob').empty();
                $.get('sublobget.php', { 'lob': lob }, function (return_data) {
                    $.each(return_data.data, function (key, value) {
                        $('#sublob').append("<option>" + value.child + "</option>");
                        $('select').formSelect();
                    });
                }, "json");
            });






        });
    </script>
</body>

</html>