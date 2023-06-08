$(document).on('click', '.js-create_chat-room-btn', function(event) {
    event.preventDefault();
    var url = $(this).attr('href');
    $.ajax({
        type: "GET",
        url: url,
      })
      .done(function(data) {
        $('.js-baseModal-content').html(data);        
        $('.js-baseModal').modal('show');
      });   
})