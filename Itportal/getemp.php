<?php

require 'conn.php';

$sql = "select email from darwin;";
// $row = $dbo->prepare($sql);
// $row->execute();
// $results = $row->fetchAll(PDO::FETCH_ASSOC);


// mysqli
$result = mysqli_query($mysqli, $sql);
// Fetch all
mysqli_fetch_all($results, MYSQLI_ASSOC);



$main = array('data' => $results);

echo json_encode($main);



?>


<script>
    $(function() {
        $.get('getemp.php', function(return_data) {
            $('input.autocomplete').autocomplete({
                data: {
                    "Apple": null,
                    "Microsoft": null,
                    "Google": null
                },
            });
        }, "json");
    });
</script>