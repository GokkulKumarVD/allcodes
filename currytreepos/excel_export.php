
 <?php

if(isset($_POST["export"]))
{

 
  $connect = new PDO("mysql:host=localhost;dbname=rms", "root", "");
  $file_name = 'Order Data.csv';
  header("Content-Description: File Transfer");
  header("Content-Disposition: attachment; filename=$file_name");
  header("Content-Type: application/csv;");

  $file = fopen('php://output', 'w');

  $header = array("Order Date", "Order No", "Amount");

  fputcsv($file, $header);

  $query = "
  SELECT * FROM order_table 
  WHERE order_date >= '".$_POST["start_date"]."' 
  AND order_date <= '".$_POST["end_date"]."' 
  ORDER BY order_date DESC
  ";
  $statement = $connect->prepare($query);
  $statement->execute();
  $result = $statement->fetchAll();
  foreach($result as $row)
  {
   $data = array();
   $data[] = $row["order_date"];
   $data[] = $row["order_number"];
   $data[] = $row["order_net_amount"];
   print_r($data);
   fputcsv($file, $data);
  }
  fclose($file);
  exit;
 
}


?>