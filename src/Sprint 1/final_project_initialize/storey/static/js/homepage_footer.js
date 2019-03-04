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
     
     
event.preventDefault(); // Prevent form from being submitted
    
      var form = $('#postarea').serializeArray();
      var paras = {}

      $('#postarea :input').each(function () {
          paras[$(this).attr('name')] = $(this).val();
      });

      $.post('/storey/editHomepageFooter/', paras)
        .done(function(data) {
          updateFooterChanges(data);
});
  });


  // The following function will help you update the contents of the
  // page based on our application's JSON response.
  function updateFooterChanges(data) {
  
    if (data['footer_isVisible']) {
      console.log("hi1")
    var promo = document.getElementById("promotion")
    if (promo.childElementCount > 0) {
      promo.removeChild(promo.lastChild);
    }

    var p = document.createElement('a')
    p.innerHTML = data['footer_promotion']
    p.href = data['footer_promotion_content']
    promo.appendChild(p);

    promo = document.getElementById("link1")
    if (promo.childElementCount > 0) {
      promo.removeChild(promo.lastChild);
    }
    var p = document.createElement('a')
    p.innerHTML = data['footer_link_1']
    p.href = data['footer_link_1_content']
    promo.appendChild(p);

    promo = document.getElementById("link2")
    if (promo.childElementCount > 0) {
      promo.removeChild(promo.lastChild);
    }
    var p = document.createElement('a')
    p.innerHTML = data['footer_link_2']
    p.href = data['footer_link_2_content']
    promo.appendChild(p);
  } else {
    console.log("h2")
    var promo = document.getElementById("promotion")
    if (promo.childElementCount > 0) {
      promo.removeChild(promo.lastChild);
    }
    promo = document.getElementById("link1")
    if (promo.childElementCount > 0) {
      promo.removeChild(promo.lastChild);
    }
    promo = document.getElementById("link2")
    if (promo.childElementCount > 0) {
      promo.removeChild(promo.lastChild);
    }
  }

  }

}); // End of $(document).ready