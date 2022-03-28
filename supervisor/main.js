
$(document).ready(function() {
  ft=1;
  $('#tier2').on('hide', function () {
    $('#button').html('<span class="glyphicon glyphicon-collapse-down"></span> Show');
  })
  $('#tier2').on('show', function () {
    $('#button').html('<span class="glyphicon glyphicon-collapse-up"></span> Hide');
  })


  // MODULE FOR THE DISPLAY CARDS //

  display_org();

  function display_org(){ //DISPLAYS THE ROOT USER INFORMATION


    $.post('data.php', function(response){

     // console.log(response);
      var blob = JSON.parse(response);
    //  console.log(blob);
      for(i = 0; i < blob.data.length; i++) {

        
       // console.log(blob.data[i]['agent_email']);
        var x =   blob.data[i]['name'];
        var a =   blob.data[i]['csat'];
        var b =   blob.data[i]['aht'];
        var c =   blob.data[i]['frt'];
        

        $("#user1").html(x);
        if(a>75){
        $("#csat").html(' <h2 style="color:#39DA19;">'+a+'</h2>'+'<span style="color:#39DA19;">'+"percent"+'</span>');
       // $("#csat1").html('<i class="far fa-smile"style="font-size:48px;color:#39DA19"></i>');
      }
        else{
          $("#csat").html(' <h2 style="color:red;">'+a+'</h2>'+'<span style="color:red;">'+"percent"+'</span>');
       //   $("#csat1").html('<i class="far fa-frown"style="font-size:48px;color:red"></i>');
        }
        
        $("#aht1").html(' <h2 style="color:#4e73df;">'+b+'</h2>'+'<span style="color:#4e73df;">'+"minutes"+'</span>');
       
        if(c>15){
          $("#frt1").html('<h2 style="color:red;">'+c+'</h2>'+'<span style="color:red;">seconds</span>');

        }
        else{
          $("#frt1").html('<h2 style="color:#39DA19;">'+c+'</h2>'+'<span style="color:#39DA19;">seconds</span>');
        }
        get_data(x);

         
      }
    });
  }
      function get_data(x){


       // console.log(x);






      }
  
  // END OF DISPLAY CARD SECTION //

  // START OF TREEVIEW //

  $.post('data.php', function(response){

      var tree_data = JSON.parse(response);

      var root_user = tree_data.data[0]['name'];

    
      
    // console.log(root_user);
      $.post('data2.php',{'postname':root_user}, function(response){

        //console.log(response);

              var bleh = JSON.parse(response);

             // console.log(response);
              for(i = 0; i < bleh.data.length; i++) {

                    var email3 = bleh.data[i]['EMAIL_ID'];

                   //console.log(email3);
                    $.post('data3.php',{postname:email3}, function(response){

                       // console.log(response);
                          var temp4 = JSON.parse(response);
                      var email_tree = temp4.data[0]['name'];
                     var csat_tree = temp4.data[0]['csat'];
                      var aht_tree =    temp4.data[0]['aht'];
                      var frt_tree = temp4.data[0]['frt'];
                        var trr = email_tree;
                     // console.log(email_tree,csat_tree,aht_tree,frt_tree);

                      

                      //view of child-1 ellements//
                      $("#tier2").append('<div class="accordion" id="accordionExample'+ft+'">'+'<div class = "card">'+'<div class="card-header" id="headingOn'
                      +'<h6 class="mb-0">'+'<div class="row" id="tier1_1" style="padding:10px;">'
                      +'<div class="col-lg-1"></div>'+'<div id ="'+email_tree+'" class="col-lg-3">'
                      +email_tree+'</div><br>'+'<div id ="'
                      +csat_tree+'" class="col-lg-2">'+csat_tree+'</div><br>'
                      +'<div id ="'+aht_tree+'" class="col-lg-2">'+aht_tree+'</div><br>'+'<div id ="'
                      +frt_tree+'" class="col-lg-2">'+frt_tree+'</div><br>'
                      +'<div class="col-lg-2">'+'<button id="search_tree_user'+ft+'" value="'
                      +trr+'" class="btn btn-primary collapsed" type="button" data-toggle="collapse" data-target="#collapsee'+ft+'" aria-expanded="true" aria-controls="collapsex"></button>'+'</div>'+'</div>'+'</h6>'+'</div>'
                      +'<div id="collapsee'+ft+'" class="collapse" aria-labelledby="headingOn" data-parent="#accordionExample'+ft+'">'+' <div class="card-body" id="child_body'+ft+'"></div>'+'</div>'+'</div>'+'</div>');
                     // $("#tier2").append('<div class="col-lg-1"></div>');
                    //  $("#tier1_1").append('<div id ="'+email_tree+'" class="col-lg-3">'+email_tree+'</div><br>');
                      //$("#tier1_1").append('<div id ="'+csat_tree+'" class="col-lg-2">'+csat_tree+'</div><br>');
                      //$("#tier1_1").append('<div id ="'+aht_tree+'" class="col-lg-2">'+aht_tree+'</div><br>');
                      //$("#tier1_1").append('<div id ="'+frt_tree+'" class="col-lg-2">'+frt_tree+'</div><br>');
                      //$("#tier1_1").append('<div class="col-lg-2">'+'<button id="search_tree_user" value="'+trr+'" class="btn btn-primary collapsed" type="button" data-toggle="collapse" data-target="#collapsee" aria-expanded="true" aria-controls="collapsex"><i class="fa fa-plus"></i></button>'+'</div>');
                      //$("#tier2").append();
                    //  $("#tier2").append('<div id="collapsee'+i+'" class="collapse" aria-labelledby="headingOn" data-parent="#accordionExample">'+' <div class="card-body"></div>'+'</div>');

                     
                    //    <div id="collapsee'+i+'" class="collapse" aria-labelledby="headingOn" data-parent="#accordionExample">
                   //   <div class="card-body">
                     //    <h6 class="mb-0"></div>  <div id = "search_childcard1" class="row"></h6>    
                    //  </div>  
              //     </div>

                       ft = ft+1; 
//
                      });
                     


                    
              }
                //CHILD 1 //

              $(document).on('click','#search_tree_user1',function(){

                var x = $(this).attr('value');
                //  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){
                             // console.log(response);
                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body1').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
                                                           // console.log(response);
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body1').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                                 // $('#child_body1').append(csat_final);
                                                                //  $('#child_body1').append(aht_final);
                                                                //  $('#child_body1').append(frt_final);

                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });

              // END OF CHILD 1 //

              // CHILD 2 //

              $(document).on('click','#search_tree_user2',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body2').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body2').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                                //  $('#child_body2').append(csat_final);
                                                                 // $('#child_body2').append(aht_final);
                                                                 // $('#child_body2').append(frt_final);

                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });

              // END OF CHILD 2 //

              // CHILD 3 //

              
              $(document).on('click','#search_tree_user3',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body3').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body3').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                                 // $('#child_body3').append(csat_final);
                                                                 // $('#child_body3').append(aht_final);
                                                                 // $('#child_body3').append(frt_final);

                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });


              // END OF CHILD 3 //

              // CHILD 4 //

              
              $(document).on('click','#search_tree_user4',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body4').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body4').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                                 

                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });

              // END OF CHILD 4 //


              // child 5 //

              $(document).on('click','#search_tree_user5',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body5').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body5').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                               
                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });


              // END OF CHILD 5 //


              // CHILD 6 //
              $(document).on('click','#search_tree_user6',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body6').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body6').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                               

                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });


              // END OF CHILD 6 //

              // CHILD 7 //
              $(document).on('click','#search_tree_user7',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body7').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body7').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                                 

                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });

              // END OF CHILD 7 //

              // CHILD 8 //

              $(document).on('click','#search_tree_user8',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body8').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body8').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                                 
                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });
              // END OF CHILD 8 //


              // CHILD 9 //

              $(document).on('click','#search_tree_user9',function(){

                var x = $(this).attr('value');
                  console.log(x);

                          //  $('#child_body1').html(x);         
                          $.post('final1.php',{postname:x}, function(response){

                                                var blah = JSON.parse(response);
                                                            //  console.log(blah.data)
                                                for(i = 0; i < blah.data.length; i++) {

                                                              // console.log('x');
                                                              //  console.log(blah.data[i]['agent_email']);
                                                
                                                var email4 = blah.data[i]['EMAIL_ID'];
                                                $('#child_body9').html('');
                                                       $.post('final2.php',{postname:email4}, function(response){
  
  
                                                                var blur = JSON.parse(response);
                                                                var email_final = blur.data[0]['name'];
                                                                var csat_final = blur.data[0]['csat'];
                                                                var aht_final = blur.data[0]['aht'];
                                                                var frt_final = blur.data[0]['frt'];
                                                               // console.log(email_final, csat_final, aht_final, frt_final);

                                                               
                                                                  $('#child_body9').append('<h6 class="mb-0"></div>'+'<div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="search_email12" class="col-lg-3">'+email_final+'</div><br>'+'<div id="search_csat12" class="col-lg-2">'+csat_final+'</div><br>'+'<div id="search_aht12" class="col-lg-2">'+aht_final+'</div><br>'+'<div id ="search_frt12" class="col-lg-2">'+frt_final+'</div><br>'+'</div><hr></h6>');
                                                                  

                                                                 
                           

                         



                          //  $('#child_body'+ft+'').append(temp5.data[i]['agent_email']);
                                                                 });

                                                  }

                                        });


              });

              // END OF CHILD 9 //

      });

  });




  // END OF TREEVIEW //


  // THE MODULE FOR THE SEARCH SEGEMENT OF THE SUPERVISOR UI //





        $("#search_button").click(function(){

              var email_id = $("#search_email").val();
            var email1 = email_id;

              $.post('search.php',{postname:email1}, function(response){

              
                var first_search = JSON.parse(response);
                var search_user_1 = first_search.data[0]['name'];
                var search_csat_1 = first_search.data[0]['csat'];
                var search_aht_1 = first_search.data[0]['aht'];
                var search_frt_1 = first_search.data[0]['frt'];
                
                search_card(search_user_1,search_csat_1,search_aht_1,search_frt_1);
                $("#search_childcard").html("");
  
              });
             // 



        });

        function search_card(a,b,c,d){

            var email1 = a;
            var csat1 = b;
            var aht1 = c;
            var frt1 = d;


            


           //$("#tier1").append('<div class="card-header" id="headingOne">');

              // $("#tier1").append('<h6 class="mb-0">');
                   
                   //  $("#tier1").append('<div class="row">');
                    $("#tier1").html("");


                                                
                             $("#tier1").append('<div class="col-lg-1"></div>');
                             $("#tier1").append('<div id ="search_email" class="col-lg-3">'+email1+'</div><br>');
                             $("#tier1").append('<div id="search_csat" class="col-lg-2">'+csat1+'</div><br>');
                             $("#tier1").append('<div id="search_aht" class="col-lg-2">'+aht1+'</div><br>');
                             $("#tier1").append('<div id ="search_frt" class="col-lg-2">'+frt1+'</div><br>');
                             $("#tier1").append('<div class="col-lg-2">'+'<button id="search_child_user" class="btn btn-primary collapsed" type="button" data-toggle="collapse" data-target="#collapsex" aria-expanded="true" aria-controls="collapsex">Expand View</button>'+'</div>');
           
                             $(document).one('click','#search_child_user',function(){

                             //  console.log(email1);
                              //  disappear();

                              
                               

                               //create ajax call//
                               $.post('search2.php',{postname:email1}, function(response){
                                // console.log(response);

                                 var email2= response;
                                 var search_2 = JSON.parse(email2);
                                 for(i = 0; i < search_2.data.length; i++){

                                      var email3 = search_2.data[i]['EMAIL_ID'];
                                      

                                  $.post('search3.php',{postname:email3}, function(response){


                                            var block = JSON.parse(response);
                                         //   console.log(block);
                                         var search_email_final =  block.data[0]['name'];
                                          var search_csat_final =  block.data[0]['csat'];
                                          var search_aht_final = block.data[0]['aht'];
                                          var search_frt_final = block.data[0]['frt'];
                                          
                                          
                                         // $('#search_childcard').append('<div class="card-body">');
                                          $('#search_childcard').append('<div id="collapsex" class="collapse" aria-labelledby="headingOne" data-parent="#accordionExample">'+'<div class="card-body w-20">'+'<h6 class="mb-0"></div><div style="padding-bottom:10px;"class="row">'+'<div class="col-lg-1"></div>'+'<div id ="'+search_email_final+'" class="search_email_final col-lg-3">'+search_email_final+'</div><br>'+'<div id="'+search_csat_final+'" class="col-lg-2">'+search_csat_final+'</div><br>'+'<div id="'+search_aht_final+'" class="col-lg-2">'+search_aht_final+'</div><br>'+'<div id ="'+search_frt_final+'" class="col-lg-2">'+search_frt_final+'</div><br>'+'</div>'+'<div class="col-lg-2"></div>'+'<hr>'+'</div></h6>'+'</div>');
                                       //   $('#search_childcard').append();
                                      //    $('#search_childcard').append();
                                       //  $('#search_childcard').append();
                                       //   $('#search_childcard').append();
                                       //   $('#search_childcard').append();
                                          
                                          $(document).on('click','#search_child_user_final',function(){

                                        //  console.log(email2);
                                                    //  search_card(search_email_final, search_csat_final, search_aht_final, search_frt_final);

                                         });
                                          

                                         

                                  });

                                 
                                 
                                  }

                               });

                             
                   
                             
                               
                           });




        }

      



  // END OF THE MODULE FOR SEARCH SEGMENT OF THE SUPERVISOR UI//


hidex();
  function hidex(){
//$('#tier2').hide();
$('#show1').hide();
 $('#show_data').html('Show');
  }    

$('#show_data').on('click', function(){

  $('#show_data').html('Hide');

  $('#tier2').toggle();
  $('#show1').toggle(); 
 // $("#search_tree_user1").html('Expand');
//  $("#search_tree_user2").html('Expand');
 // $("#search_tree_user3").html('Expand');
//  $("#search_tree_user4").html('Expand');
 // $("#search_tree_user5").html('Expand');
 // $("#search_tree_user6").html('Expand');
//  $("#search_tree_user7").html('Expand');
 // $("#search_tree_user8").html('Expand');
 // $("#search_tree_user9").html('Expand');


 

 });

 

 $(".collapse").on('show.bs.collapse',function(){

  $('#show_data').html('Hide');
  
  //$("#search_tree_user1").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user2").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user3").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user4").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user5").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user6").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user7").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user8").html('<i class="fa fa-minus" aria-hidden="true"></i>');
  //$("#search_tree_user9").html('<i class="fa fa-minus" aria-hidden="true"></i>');
 });

 $(".collapse").on('hide.bs.collapse',function(){

  $('#show_data').html('Show');
 // $("#search_tree_user1").html('<i class="fa fa-plus" aria-hidden="true"></i>');
 // $("#search_tree_user2").html('<i class="fa fa-plus" aria-hidden="true"></i>');
//  $("#search_tree_user3").html('<i class="fa fa-plus" aria-hidden="true"></i>');
//  $("#search_tree_user4").html('<i class="fa fa-plus" aria-hidden="true"></i>');
//  $("#search_tree_user5").html('<i class="fa fa-plus" aria-hidden="true"></i>');
 // $("#search_tree_user6").html('<i class="fa fa-plus" aria-hidden="true"></i>');
 // $("#search_tree_user7").html('<i class="fa fa-plus" aria-hidden="true"></i>');
 // $("#search_tree_user8").html('<i class="fa fa-plus" aria-hidden="true"></i>');
 // $("#search_tree_user9").html('<i class="fa fa-plus" aria-hidden="true"></i>');
 });

 $("search_tree_user1").on('click',function(){

      $("search_tree_user1").html('<i class="fa fa-minus" aria-hidden="true"></i>');


 });


   



  
  });