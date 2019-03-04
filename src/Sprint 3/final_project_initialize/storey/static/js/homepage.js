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

  $( 'button#submit_header' ).on('click', function(event)
  {
     event.preventDefault(); // Prevent form from being submitted
     var data = new FormData($('form#postarea_1').get(0));
     $.ajax(
     {
      url: 'editHomepageHeader',
      type: 'POST',
      data: data,
      cache: false,
      processData: false,
      contentType: false,
      success: function(data)
      { 
        $('#headimage').attr('style','background-image:url(/static/media/'+data['header_logo']);
        $('#headertitle').empty();
        var text   = $("<span>",{"text": data['header_text'],}).appendTo('#headertitle');
      }
    });
     return false;
  });

  $( 'button#submit_demo' ).on('click', function(event)
  {
     event.preventDefault(); // Prevent form from being submitted
     var data = new FormData($('form#postarea_2').get(0));
     console.log(data);
     $.ajax({
      url: 'editHomepageDemo',
      type: 'POST',
      data: data,
      cache: false,
      processData: false,
      contentType: false,
      success: function(data)
      { 
        $('#product_demo_img_1').attr('style','background-image:url(/static/media/'+data['demo_pic_1']);
        $('#product_demo_img_2').attr('style','background-image:url(/static/media/'+data['demo_pic_2']);
        $('#description_1').empty();
        var description_1   = $("<span>",{"text": data['description_1'],}).appendTo('#description_1');
        $('#description_2').empty();
        var description_2   = $("<span>",{"text": data['description_2'],}).appendTo('#description_2');
        $('#product_name_1').empty();
        var product_name_1   = $("<span>",{"text": data['name_1'],}).appendTo('#product_name_1');
        $('#product_name_2').empty();
        var product_name_2   = $("<span>",{"text": data['name_2'],}).appendTo('#product_name_2');
      }
   });
  });


  $( 'button#submit_navbar' ).on('click', function(event)
 {
   event.preventDefault(); // Prevent form from being submitted
   var data = new FormData($('form#postarea_3').get(0));
   $.ajax({
    url: 'editHomepageNavbar',
    type: 'POST',
    data: data,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data)
    { 
      $('#navbar').empty();
      var img = $ ("<img>",{"src":"/static/media/"+data['navbar_logo'],
        "width":data['navbar_width'],"height":data['navbar_height']}).appendTo('#navbar');
      var commenttext   = $("<span>",{ "text" : data['navbar_text'],"class" : "navbartext ",}).appendTo('#navbar');
    }
   });
   return false;
 });

  $( 'button#submit_footer' ).on('click', function(event)
 {
   event.preventDefault(); // Prevent form from being submitted
   var data = new FormData($('form#postarea_4').get(0));
   $.ajax({
    url: 'editHomepageFooter',
    type: 'POST',
    data: data,
    cache: false,
    processData: false,
    contentType: false,
    success: function(data)
    { 
      $('#footer_block').empty();
      var shop_name    = $("<div>",{ "text" : data['footer_Shopname'],}).appendTo('#footer_block');
      var company_name = $("<div>",{ "text" : data['footer_Company'],}).appendTo('#footer_block');
    }
   });
   return false;
 });


  $('#postarea_1').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted
    });
  $('#postarea_2').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted
    });
  $('#postarea_3').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted
    });
  $('#postarea_4').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted
    });
}); 

