// The boilerplate code below is copied from the Django 1.10 documentation.
// It establishes the necessary HTTP header fields and cookies to use
// Django CSRF protection with jQuery Ajax requests.

$(document).ready(function() {  // Runs when the document is ready

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

  $('#postarea').on('submit', function(event) {
     /**
      event.preventDefault(); // Prevent form from being submitted

      var form = $('#postarea').serializeArray();
      var paras = {}

      $('#postarea :input').each(function () {
          paras[$(this).attr('name')] = $(this).val();
      });
     */
      
/**
    event.preventDefault();

  
  var $form = $( this ), url = $form.attr( 'action' );

  var posting = $.post( url, { name: $('#name').val()} );
  */

  /* Alerts the results */
  /**

  posting.done(function( data ) {
    console.log(data['header_descrpition']);
          console.log(data['header_logo']);
    updateChanges(data);

  });

  

/**
      $.post('/storey/editHomepageHeader/')
        .done(function(data) {
          console.log("hi2");
          console.log(data['header_descrpition']);
          console.log(data['header_logo']);
          updateChanges(data);
        });
*/
  });


  // The following function will help you update the contents of the
  // page based on our application's JSON response.
  function updateChanges(data) {
    console.log("hi1");
    var img_url = '<img src="' + data['header_logo']
        + '" alt="" width="100" height="100">';
    console.log(img_url);
    
    var elem = document.createElement("img");
    elem.setAttribute("src", "../" + data['header_logo']);
    elem.setAttribute("width", data['header_width']);
    elem.setAttribute("height", data['header_height']);
    var logo_img = document.getElementById("logo_img")
    /**
    if (logo_img.childElementCount > 0) {
      logo_img.removeChild(logo_img.lastChild);
    }
    */
   logo_img.appendChild(elem);

  }

}); // End of $(document).ready