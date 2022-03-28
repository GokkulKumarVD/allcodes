<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Document</title>
</head>

<body>

    <div id="readydemo">
        <button id="clickme">click</button>
    </div>


    <!-- <script src="C:\xampp\htdocs\jql\src\jquery-3.6.0.min.js"></script> -->
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script>
        $(document).ready(function() {
            // $('#readydemo').text("Hello world!");
            $("#clickme").click(function() {
                $.ajax({
                    url: 'https://api.jsonbin.io/b/6117bb0ee1b0604017afdd29',
                    type: 'GET',
                    dataType: 'json',
                    timeout: 2500,
                    success: function(result) {
                        console.log('complete with result:', result)
                    },
                    error: function(result) {
                        console.log('complete with error');
                    },
                    complete: function() {
                        console.log('complete')
                    }

                });
            });

        });
    </script>
</body>

</html>