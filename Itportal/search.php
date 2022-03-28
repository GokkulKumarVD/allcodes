<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">


    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <?php include 'header.php' ?>

    <div class="card">
        <div class="card-content">
            <form action="" method="post">
                <div class="container center">
                    <div class="row">
                        <div class="input-field col l5 ">
                            <select id="searchby">
                                <option value="" disabled selected>Choose criteria</option>
                                <option value="laptopid">Laptop ID</option>
                                <option value="assignedby">Assigned by</option>
                                <option value="approvedby">Approved by (not functional)</option>
                                <option value="grade">Grade (not functional)</option>
                                <option value="assignedto">Assigned to (not functional)</option>
                            </select>
                            <label>Search by</label>
                        </div>
                        <div class="col l5 ">
                            <div class="input-field">
                                <input type="text" name="search" id="search">
                                <label for="search">Enter details</label>
                            </div>
                        </div>
                        <br>
                        <div class="col statshide" id="stats">
                            <p>
                                <label>
                                    <input name="stats" type="radio" value="complete" checked />
                                    <span>Complete &nbsp; &nbsp;</span>
                                </label>
                            </p>
                            <p>
                                <label>
                                    <input name="stats" type="radio" value="seggregate" />
                                    <span>Seggregate </span>
                                </label>
                            </p>
                        </div>
                    </div>

                    <div class="input-field">
                        <input type="submit" class="btn z-depth-2" id="submit">
                    </div>
                </div>
        </div>
        </form>
    </div>
    </div>

    <div class="laptopid_table" id="laptopid_id">
        <div class="card z-depth-2">
            <table class="highlight centered">
                <thead>
                    <tr>
                        <th>Assigned to</th>
                        <th>Assigned by</th>
                        <th>Approved by</th>
                        <th>Work location</th>
                        <th>Grade</th>
                        <th>Date</th>
                        <th>Price</th>
                    </tr>
                </thead>

                <tbody id="loadhere_laptopid_table">
                    <!-- <tr>
                        <td>Gokkul</td>                   
                        <td>Vignesh</td>
                        <td>Santosh</td>
                        <td>Maruti chambers</td>
                        <td>4</td>
                        <td>2021-06-02</td>
                        <td>90000</td>
                    </tr> -->
                    <!-- pushing rows here by jquery -->
                </tbody>
            </table>
        </div>
    </div>

    <div class="assignedby_table" id="assignedby_table_id">
        <div class="card z-depth-2">
            <table class="highlight centered">
                <thead>
                    <tr>
                        <th>Assigned to</th>
                        <th>Approved by</th>
                        <th>Work location</th>
                        <th>Grade</th>
                        <th>Date</th>
                        <th>Price</th>
                    </tr>
                </thead>

                <tbody id="loadhere_assignedby_table">
                    <tr>
                        <!-- <td>Gokkul</td>                   
                        <td>Santosh</td>
                        <td>Maruti chambers</td>
                        <td>4</td>
                        <td>2021-06-02</td>
                        <td>90000</td> -->
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="hidestats" id="rmstats">
        <div class="container">
            <div class="row center">
                <div class="card col l12">
                    <div class="card-title">
                        <h5 class="grey-text" style="font-family: 'Bebas Neue', cursive; margin-top: 50px;">Count of laptop </h5>
                    </div>
                    <div class="card-content" id="count_laptop">
                        <!-- <h2>100</h2> -->
                    </div>
                </div>
            </div>
        </div>
    </div>

    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>

    <script>
        AOS.init({
            opacity: 100
        });
    </script>

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    <script>
        $(document).ready(function() {
            $('select').formSelect();

            $('#searchby').change(function(e) {
                $('#laptopid_id').addClass("laptopid_table");
                $('#assignedby_table_id').addClass("assignedby_table");
                $('#rmstats').addClass("hidestats");
                e.preventDefault();
                var searchby = $('#searchby').val();
                if (searchby === 'assignedby') {
                    $('#stats').removeClass("statshide");
                } else {
                    $('#stats').addClass("statshide");
                    var stats = 'nothing';
                }
            });


            $('#submit').click(function(e) {
                e.preventDefault();
                $('#loadhere_assignedby_table').empty();
                var searchby = $('#searchby').val();
                var details = $('#search').val();

                if (searchby === 'assignedby') {
                    var selected = $('input[name="stats"]:checked').val();
                }


                if (searchby === 'laptopid') {
                    $.get('detailsfetch.php', {
                        'searchby': searchby,
                        'details': details
                    }, function(return_data) {
                        $('#laptopid_id').removeClass("laptopid_table");
                        $.each(return_data.data, function(key, value) {
                            $('#loadhere_laptopid_table').append("<tr data-aos='flip-down'><td>" + value.email + "</td><td>" + value.assignedby + "</td><td>" + value.approvedby + "</td><td>" + value.work_location + "</td><td>" + value.grade + "</td><td>" + value.assigned_date + "</td><td>" + value.price + "</td></tr>");
                            $('select').formSelect();
                        });
                    }, "json");
                } else if (searchby === 'assignedby' & selected === 'complete') {
                    $.get('detailsfetch.php', {
                        'searchby': searchby,
                        'details': details,
                        'selected': selected
                    }, function(return_data) {
                        $('#assignedby_table_id').removeClass("assignedby_table");
                        $.each(return_data.data, function(key, value) {
                            $('#loadhere_assignedby_table').append("<tr data-aos='flip-down'><td>" + value.email + "</td><td>" + value.approvedby + "</td><td>" + value.work_location + "</td><td>" + value.grade + "</td><td>" + value.assigned_date + "</td><td>" + value.price + "</td></tr>");
                            $('select').formSelect();
                        });
                    }, "json");
                } else if (searchby === 'assignedby' & selected === 'seggregate') {
                    $.get('detailsfetch.php', {
                        'searchby': searchby,
                        'details': details,
                        'selected': selected
                    }, function(return_data) {
                        $('#rmstats').removeClass("hidestats");
                        $.each(return_data.data, function(key, value) {
                            $('#count_laptop').empty().append("<h2 data-aos='flip-down'>" + value.count + "</h2>");
                            console.log('working');
                            $('select').formSelect();
                        });
                    }, "json");
                }
            });
        });
    </script>

</body>

</html>