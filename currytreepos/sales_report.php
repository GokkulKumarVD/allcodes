<?php
ob_start();
include('rms.php');


$object = new rms();

if(!$object->is_login())
{
    header("location:".$object->base_url."");
}

if(!$object->is_master_user())
{
    header("location:".$object->base_url."dashboard.php");
}

include('sidenav.php');
$con = mysqli_connect("localhost", "root", "","rms");
//excel code logic



//code to retrieve data for table display
// $query = "
// SELECT * FROM order_table 
// ORDER BY order_date DESC;
// ";

// $statement = $connect->prepare($query);
// $statement->execute();
// $result = $statement->fetchAll();

ob_end_flush();
?>


    
                    <!-- Page Heading -->
                    <h1 class="h3 mb-4 text-gray-800">Sales Report</h1>

   <!-- Search filter -->
   <form method='post' action=''>
       
     Start Date <input type='text' class='dateFilter' name='fromDate' readonly value='<?php if(isset($_POST['fromDate'])) echo $_POST['fromDate']; ?>'>
 
     End Date <input type='text' class='dateFilter' name='endDate' readonly value='<?php if(isset($_POST['endDate'])) echo $_POST['endDate']; ?>'>

     <input type='submit' name='but_search' value='Search'>
   </form>
<br><br><br>
                    <!-- DataTales Example -->
                    <span id="message"></span>
                    <div class="card shadow mb-4">
                        <div class="card-header py-3">
                        	<div class="row">
                            	<div class="col">
                            		<h6 class="m-0 font-weight-bold text-primary">report</h6>
                            	</div>
                            	
                            </div>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <table class="table table-bordered" id="salestable" width="100%" cellspacing="0">
                                    <thead>
                                        <tr>
                                            <th>Order Date</th>
                                            <th>Order Number</th>
                                            <th>Amount</th>
                                      
                                        </tr>
                                    </thead>
                                    <tbody>
                                    <?php
       $emp_query = "SELECT * FROM order_table WHERE 1 ";

       // Date filter
       if(isset($_POST['but_search'])){
          $fromDate = $_POST['fromDate'];
          $endDate = $_POST['endDate'];

          if(!empty($fromDate) && !empty($endDate)){
             $emp_query .= " and order_date 
                          between '".$fromDate."' and '".$endDate."' ";
          }
        }

        // Sort
        $emp_query .= " ORDER BY order_date DESC";
        $employeesRecords = mysqli_query($con,$emp_query);
        $total_amount = 0;
        // Check records found or not
        if(mysqli_num_rows($employeesRecords) > 0){
           
          while($empRecord = mysqli_fetch_assoc($employeesRecords)){
           
            $orderdate = $empRecord['order_date'];
            $orderno = $empRecord['order_number'];
            $amount = $empRecord['order_gross_amount'];
            $total_amount += $empRecord['order_gross_amount'];
           

            echo "<tr>";
            echo "<td>". $orderdate ."</td>";
            echo "<td>". $orderno ."</td>";
            echo "<td>". $amount ."</td>";
            echo "</tr>";
          }
        }else{
          echo "<tr>";
          echo "<td colspan='4'>No record found.</td>";
          echo "</tr>";
        }
        ?>	
    
                                    </tbody>
                                
                                    <tfoot>
                                            <tr>
                                             <th>Order Date</th>
                                            <th>Order Number</th>
                                            <th>Amount</th>
                                            </tr>
        </tfoot>
                                </table>
                            </div>
                        </div>
                        <h3 style="margin: left 40px;">Total Sales: <?php echo $total_amount; ?></h3>
                    </div>


                <?php
                include('footer.php');
                ?>


<script>

$(document).ready(function(){
 $('.dateFilter').datepicker({
  todayBtn:'linked',
  format: "yyyy-mm-dd",
  autoclose: true
 });
});

$(document).ready(function(){
var dataTable = $('#salestable').DataTable({ 
    dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ]
    });
});

</script>

<script src="https://code.jquery.com/jquery-3.5.1.js"></script>
<script src="https://cdn.datatables.net/1.10.25/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.7.1/js/dataTables.buttons.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>

<script src="https://cdn.datatables.net/buttons/1.7.1/js/buttons.html5.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.7.1/js/buttons.print.min.js"></script>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.6.4/css/bootstrap-datepicker.css" />
  <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.6.4/js/bootstrap-datepicker.js"></script>

 </head>
 <body>