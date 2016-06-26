$(document).ready(function() {
    $('#list').click(function(event){
        event.preventDefault();$('#listings .item').addClass('');
    });
    $('#grid').click(function(event){
        event.preventDefault();$('#listings .item').removeClass('list-group-item');
        $('#listings .item').addClass('grid-group-item');
    });
    $('#thumb').click(function(event){
        event.preventDefault();$('#listings .item').removeClass('list-group-item');
        $('#listings .item').addClass('grid-group-item');
    });

});
