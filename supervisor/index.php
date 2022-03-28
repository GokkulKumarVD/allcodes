<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>BOW: Production Score</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.min.css" rel="stylesheet">
  <!-- MDB -->
<link
  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.6.0/mdb.min.css"
  rel="stylesheet"
/>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

<!--     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>-->
<!--    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>-->
<!--    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>-->


    <style>
    .scrollable-menu {
            height: auto;
            max-height: 58.5vh;
            overflow-x: hidden;
        }
        .flip-card {
  background-color: transparent;
  width: 300px;
  height: 300px;
  perspective: 1000px;
}

.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.flip-card-front {
  background-color: #bbb;
  color: black;
}

.flip-card-back {
  background-color: #2980b9;
  color: white;
  transform: rotateY(180deg);
}
    </style>
     
</head>

<body id="page-top">

  <!-- Page Wrapper -->
  <div id="wrapper">

    <!-- Sidebar -->
      <!-- <?php require 'src/sidebar.php'; ?> -->
    <!-- End of Sidebar -->
      
    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">

      <!-- Main Content -->
      <div id="content">

        <!-- Topbar -->
          <?php require 'src/navbar.php'; ?>
        <!-- End of Topbar -->
         
        <!-- Begin Page Content -->
        <div class="container-fluid">
            <div class = row>

                     
            <div class="col-lg-4">
                        <div class="card">
                          <div class="card-header" style="background-color:white;text-align:center;"><h6 style="color: #4e73df;">Average First Response Time</h6></div>
                          <div id ="csat" class ="card-body" id="chart1" style="background-color:white; text-align:center;">
                                  </div>
                        </div>
      </div>
      
      <div class="col-lg-4">
                        <div class="card">
                          <div class="card-header" style="background-color:white;text-align:center;"><h6 style="color: #4e73df;">Average First Response Time</h6></div>
                          <div id ="frt1" class ="card-body" id="chart1" style="background-color:white; text-align:center;">
                                  </div>
                        </div>
      </div>
      <div class="col-lg-4">
                        <div class="card">
                          <div class="card-header"style="background-color:white;text-align:center;"><h6 style="color: #4e73df;">Average Handling Time</h6></div>
                          <div id = "aht1"class ="card-body" id="chart1"style="background-color:white; text-align:center;">
                          
                          </div>
                        </div>
                        
      </div>
            </div>
            
          <br><br>

        <div class="w-20 border">
                 <h6 class="pt-3 pl-3 flex-body" style="background-color:#4e73df; color:white;padding-top:10px;padding-bottom:10px;">
                 <div class="row">
                   <div class="col-lg-11">
                     Report<br><br>
                  
                    </div>
                    <div class="col-lg-1">

                          <button id = "show_data" class="btn btn-primary" data-toggle="collapse" data-target="#tier2">Show</button>
                       
                    </div>
                
                  </div>
                  
                  </h6>
               
                 
                  <div class="row" id="show1">
                                                                  <div class="col-lg-1"></div>
                                                                 <div class="col-lg-3" style="color:#1266f1;"><strong>&nbsp;&nbsp;&nbsp;&nbsp;Email Address</strong></div><br>
                                                                 <div class="col-lg-2"style="color:#1266f1;"> <strong>Average CSAT(%)</strong></div><br>
                                                                 <div class="col-lg-2" style="color:#1266f1;"><strong>Average FRT</strong></div><br>
                                                                 <div class="col-lg-2" style="color:#1266f1;"><strong>Average AHT</strong></div><br>
         <br>                      
         
                 <!-- THIS IS WHERE THE ITERATION IS GOING TO TAKE PLACE OF THE COLLAPSIBLE -- > -->

        <div id="tier2" class="collapse">
         
            

              <!-- END OF CARD HEADER -->

                                        <!-- CARD BODY -- THIS SEGMENT WOULD CONSIST OF THE CHILD ELEMENTS AND THE ATTEMPT FOR RECURSION WILL BE MADE IN THIS SEGMENT -->

                                       


                                        <!-- END OF CARD BODY - THE PREDOMINANANT FUNCTIONALITY OF RECURSION -->

      </div>

  <!-- THIS IS WHERE IT ENDS --->

        </div>


                 <!-- THIS IS THE REPLACEMENT--
                  
                  <div class="accordion" id="accordionExample">
                  <div class="row">
                                                                  <div class="col-lg-1"></div>
                                                                 <div class="col-lg-3" style="color:#4e73df;"><strong>&nbsp;&nbsp;&nbsp;&nbsp;Email Address</strong></div><br>
                                                                 <div class="col-lg-2" style="color:#4e73df;" ><strong>Average CSAT(%)</strong></div><br>
                                                                 <div class="col-lg-2" style="color:#4e73df;" ><strong>Average FRT</strong></div><br>
                                                                 <div class="col-lg-2" style="color:#4e73df;" ><strong>Average AHT</strong></div><br>
      </div>   <br>                                           
                                            <div class="card">
                                                  <div class="card-header" id="headingOne">
                                                           <h6 class="mb-0">
                                                             <div class="row">
                                                                  <div class="col-lg-1"></div>
                                                                 <div id ="user1" class="col-lg-3"></div><br>
                                                                 <div id="csat1" class="col-lg-2"></div><br>
                                                                 <div id="aht0" class="col-lg-2"></div><br>
                                                                 <div id ="frt0" class="col-lg-2"></div><br>
                                                                  <div class="col-lg-2">
                                                                     <button id="rootuser" class="btn btn-primary collapsed" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                                                            Expand View
         
                                                                      </button></div>
                                                                 </div>        
      
                                                            </h6>
                                                   </div>-->

                                                 <!--  <div class="card-header" id="headingTwo">
                                                           <h6 class="mb-0">
                                                             <div class="row">
                                                                  <div class="col-lg-1"></div>
                                                                 <div id ="user" class="col-lg-3"></div><br>
                                                                 <div id="csat" class="col-lg-2"></div><br>
                                                                 <div id="aht1" class="col-lg-2"></div><br>
                                                                 <div id ="frt1" class="col-lg-2"></div><br>
                                                                  <div class="col-lg-2">
                                                                     <button id="rootuser2" class="btn btn-primary collapsed" type="button" data-toggle="collapse" data-target="#collapsex" aria-expanded="true" aria-controls="collapsex">
                                                                            Expand View
         
                                                                      </button></div>
                                                                 </div>        
      
                                                            </h6>
                                                   </div> -->
<!--
                                                   <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
                                                           <div class="card-body">
                                                           <h6 class="mb-0">
                                                                 
                                                                    
                                                                  
      </div>  <div id = "childcard" style="padding-bottom:10px;"class="row">
                                                                  
                                                                 
                                                          </h6>    
                                                                     </div>  
                                                                        </div>
    <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
      <div class="card-body">
      <h6 class="mb-0">
                                                                 
                                                                    
                                                                  
      </div>    <div id = "collapseTwo1" style="padding-bottom:10px;"class="row"> 
                                                                 
                                                                
                                                         </h6>    
       
      </div>
    </div>
  </div>
  
  
</div>

                   
                  
</div>

<br><br> -->


<!-- THIS IS WHERE THE REPORT TREE ENDS -- > --->

<br><br>
    <!-- THIS IS FOR THE TREE SEARCH-->

    <div class="w-20 border">
                 <h6 class="pt-3 pl-3" style="background-color:#4e73df; color:white;"><strong></strong><div class="search-container">
    
        <form action="search.php" method="POST">
        <div class="row">
      <div class="col-lg-3">           
      <input id = "search_email" class = "form-control" type="text" placeholder="Enter Email Address" name="search">
      </div>
      <div class="col-lg-2">
      <button type="button" class="btn btn-primary" id="search_button">Search</button>
      </div>
      </div>
      
    </form><br>
      
  </div></h6>
                  
                  <div class="accordion" id="accordionExample">
                  <div class="row">
                                                                  <div class="col-lg-1"></div>
                                                                 <div class="col-lg-3" style="color:#1266f1;"><strong>&nbsp;&nbsp;&nbsp;&nbsp;Email Address</strong></div><br>
                                                                 <div class="col-lg-2"style="color:#1266f1;"> <strong>Average CSAT(%)</strong></div><br>
                                                                 <div class="col-lg-2" style="color:#1266f1;"><strong>Average FRT</strong></div><br>
                                                                 <div class="col-lg-2" style="color:#1266f1;"><strong>Average AHT</strong></div><br>
      </div>   <br>                                           
                                       <!--     <div class="card">
                                                  <div class="card-header" id="headingOne">
                                                           <h6 class="mb-0">
                                                             <div class="row">
                                                                  <div class="col-lg-1"></div>
                                                                 <div id ="user" class="col-lg-3"></div><br>
                                                                 <div id="csat" class="col-lg-2"></div><br>
                                                                 <div id="aht1" class="col-lg-2"></div><br>
                                                                 <div id ="frt1" class="col-lg-2"></div><br>
                                                                  <div class="col-lg-2">
                                                                     <button id="rootuser" class="btn btn-primary collapsed" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                                                            Expand View
         
                                                                      </button></div>
                                                                 </div>        
      
                                                            </h6>
                                                   </div>

                                                   <div id="collapseOne" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">
                                                           <div class="card-body">
                                                           <h6 class="mb-0">
                                                                 
                                                                    
                                                                  
      </div>  <div id = "childcard" style="padding-bottom:10px;"class="row">
                                                                  
                                                                 
                                                          </h6>    
                                                                     </div>  
                                                                        </div>
    <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
      <div class="card-body">
      <h6 class="mb-0">
                                                                 
                                                                    
                                                                  
      </div>    <div id = "collapseTwo1" style="padding-bottom:10px;"class="row"> 
                                                                 
                                                                
                                                         </h6>    
       
   </div> -->


    
    
    
  </div>
  
  <!-- THIS IS WHERE THE ITERATION IS GOING TO TAKE PLACE OF THE COLLAPSIBLE -- > -->

        <div class="card">
           <div class="card-header" id="headingOne">
                                          <h6 class="mb-0">
                                              <div id = "tier1" class="row">

                                              </div>
                                          </h6>
            </div>
            <div id = "search_childcard">
              <!-- END OF CARD HEADER --->

                                        <!-- CARD BODY -- THIS SEGMENT WOULD CONSIST OF THE CHILD ELEMENTS AND THE ATTEMPT FOR RECURSION WILL BE MADE IN THIS SEGMENT -->

                                        
                                         
                                              </h6>    
                                           </div>  
                                        </div>


                                        <!-- END OF CARD BODY - THE PREDOMINANANT FUNCTIONALITY OF RECURSION -->

     

  <!-- THIS IS WHERE IT ENDS --->



</div>

                   
                  
</div>

        </div>  
        <!-- /.container-fluid -->

      </div>
      <!-- End of Main Content -->

      <!-- Footer -->
      <footer class="sticky-footer bg-white">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <span>Copyright &copy; Bank of Wisdom v.0.2 &nbsp;&nbsp;|&nbsp;&nbsp; <a href="mailto:sourav.verma@swiggy.in">Sourav Verma</a> &nbsp;&nbsp;|&nbsp;&nbsp; <a href="mailto:rahul.kp@swiggy.in">Rahul K Pal</a></span>
          </div>
        </div>
      </footer>
      <!-- End of Footer -->

    </div>
    <!-- End of Content Wrapper -->

  </div>
  <!-- End of Page Wrapper -->

  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>

  <!-- Logout Modal-->
  <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
          <button class="close" type="button" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
          </button>
        </div>
        <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
        <div class="modal-footer">
          <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
          <a class="btn btn-primary" href="../login/pages/logout.php">Logout</a>
        </div>
      </div>
    </div>
  </div>

 <!-- Bootstrap core JavaScript-->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>

  <!-- Core plugin JavaScript-->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Custom scripts for all pages-->
  <script src="js/sb-admin-2.min.js"></script>

  <!-- Page level plugins -->
  <script src="vendor/chart.js/Chart.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-treeview/1.2.0/bootstrap-treeview.min.js"></script>

  <!-- Page level custom scripts -->
  <script src="js/demo/chart-area-demo.js"></script>
  <script src="js/demo/chart-pie-demo.js"></script>
  <script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>


  <script src ="jquery.js"></script>  
  <!-- MDB -->
<script
  type="text/javascript"
  src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/3.6.0/mdb.min.js"
></script>
<script src = "main.js"></script>


   

</body>

</html>
