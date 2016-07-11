
// yeah, i dont know what I am doing here....

$(document).ready(function(){
    $('btn-group a:contains("listb")').prop('selected',true);
    $("#listb").click(function(){
        $("#list").show();
        $("#grid").hide();
        $("#thumb").hide();
    });
    $("#gridb").click(function(){
        $("#grid").show();
        $("#list").hide();
        $("#thumb").hide();
    });
    $("#thumbb").click(function(){
        $("#thumb").show();
        $("#list").hide();
        $("#grid").hide();
    });
});

// http://bootsnipp.com/snippets/featured/list-grid-view
// $(document).ready(function() {
//     $('#list').click(function(event){
//         event.preventDefault();$('#listings .item').addClass('');
//     });
//     $('#grid').click(function(event){
//         event.preventDefault();$('#listings .item').removeClass('panel panel-default panel-body thumb-parent thumbnail col-md-3 col-md-9 thumb-text');
//         $('#listings .item').addClass('col-md-3 thumbnail caption');
//     });
//     $('#thumb').click(function(event){
//         event.preventDefault();$('#listings .item').removeClass('col-md-4 thumbnail caption');
//         $('#listings .item').addClass('panel panel-default panel-body thumb-parent thumbnail col-md-3 col-md-9 thumb-text');
//     });
//
// });
