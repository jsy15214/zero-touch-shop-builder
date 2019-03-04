// The boilerplate code below is copied from the Django 1.10 documentation.
// It establishes the necessary HTTP header fields and cookies to use
// Django CSRF protection with jQuery Ajax requests.

$( document ).ready(function() {  // Runs when the document is ready
 
  // using jQuery
  // https://docs.djangoproject.com/en/1.10/ref/csrf/

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });


 $( 'button#submit_navbar' ).on('click', function(event)
 {
     event.preventDefault(); // Prevent form from being submitted
   console.log('test');
   var data = new FormData($('form#postarea').get(0));
   console.log(data);
   $.ajax({
    url: 'editNavbar',
    type: 'POST',
    data: data,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data)
    {
      console.log('success');
      console.log(data);
      $('#navbar').empty();
      var img = '<img src="/storey/photo/';
      img += data['current_navbar_id'];
      img += '?';
      img += new Date().getTime();
      img += '" width=';
      img += data['navbar_width'];
      img += 'px height='
      img += data['navbar_height'];
      img += 'px >';
      console.log(img);
      $( '#navbar' ).append(img);
      var commenttext   = $("<span>",{
        "text"  : data['navbar_text'],
        "class" : "navbartext ",
      }).appendTo('#navbar');
    }
   });
   return false;
 });


  $('#postarea').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted
  });

}); 
