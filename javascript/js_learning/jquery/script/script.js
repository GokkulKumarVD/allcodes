// $("header nav  li:first").css({border:" 3px solid red"});

// ----------------------------------------

// var wrapper = '<div class="wrapper">';
// var wrapped = true;

// $('.button')[0].onclick  = function(){
//     if (wrapped === true) {
//         $('section').unwrap();
//         $('.button').text('wrap');
//         wrapped = false;
//     }else{
//         $('section').wrapAll(wrapper);
//         $('.button').text('Unwrap');
//         wrapped = true;
//     }
// }


// ----------------------------------------------
// $('.button').empty();
// $('#points-of-sale').empty();

// -----------------------------------------------

// $('.button').remove();
// $('#points-of-sale').remove();




// --------------------------

// $('#lead-banner a')[0].onclick = function(){
//     $('#points-of-sale').toggleClass("open");
//     return false;
// }

// ===========================================
// var list = $('#points-of-sale li');
// console.log(list);


// $(list).on("click", function() {
//     $(this).css({"background": "pink"});
//     list.off("click");
//   });

//   ------------------------------------------


//   $("#lead-banner").on("click",function(){
//     alert('you clicked me');
//     $("#lead-banner").off("click");
//   });

// -----------------------------------------------


// $("*").on("click", function(e){
//     e.stopPropagation()
//     console.log(e.pageX);
//     console.log(e.type);

// });


// -------------------------------------------

$("#clients h2").on("click", function () {

    $(this).animate({ "height": "100px", "width": "500px" }, 1000, function () {
        console.log('done');
    });

});


// ------------------------------------------

$("#clients h2").on("click", function () {

    $(this).fadeTo(2000, 0.2)
        .fadeTo(2000, 0.8);

    // $(this).fadeOut(3000, function () {
    //     console.log('fadedin');
    // });

    // $(this).fadeIn(1000, function () {
    //     console.log('fadedin');
    // });


});


// -----------------------------------------------

$("img[alt=map]").on("click", function () {


    // $(this).hide(1000).show(1000);

    $("#contact h2").toggle(1000);

})


// -----------------------------------------------------

// $("blockquote").fadeOut();



var blockquote = $("blockquote");
var blockquotecount = 0;

function next() {

    $($("blockquote")[blockquotecount]).fadeOut(2000, function () {

        if (blockquotecount == blockquote.length - 1) {
            blockquotecount = 0;
        } else {
            blockquotecount++;
        }

        $($("blockquote")[blockquotecount]).fadeIn();

    });

}

setInterval(next, 3000);

// --------------------------------------------------------

var items = $("#points-of-sale li");

items.on("click", function () {
    $(this).find("p").slideToggle();
    console.log($(this));
});



// console.log($("#points-of-sale li p"));