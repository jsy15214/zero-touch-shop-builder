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
  $.ajax({
	  url: 'demo_info',
	  type: 'GET',
	  success: function(data)
	  {
		  return;
		  $('#category_name_1').remove();
		  $('#category_name_2').remove();
		  $('#description_2').remove();
		  $('#description_1').remove();
		  c1_name = '<h1 class="display-4 font-italic" id="category_name_1">'+data['name_1']+'</h1>';
          c1_des = '<p class="lead my-3" style="color: white" id="description_2">' + data['description_1'] + '</p>'
		  $('#c1_container').prepend(c1_des);
		  $('#c1_container').prepend(c1_name);
		  c2_name = '<h1 class="display-4 font-italic" id="category_name_2">'+data['name_2']+'</h1>';
          c2_des = '<p class="lead my-3" style="color: white" id="description_2">' + data['description_2'] + '</p>'
		  $('#c2_container').prepend(c2_des);
		  $('#c2_container').prepend(c2_name);

		  $('div#c1_container_img').empty();
		  $('div#c2_container_img').empty();
		  var tima = new Date();
		  img_1 = '<img src=/storey/demo_picture_1/' + data['username'] + '?' + tima.getTime() + ' class="inline-block" width="200" height="200">'
		  console.log(img_1);
		  $('div#c1_container_img').append(img_1);
		  img_2 = '<img src=/storey/demo_picture_2/' + data['username'] + '?' + tima.getTime() + ' class="inline-block" width="200" height="200">'
		  $('div#c2_container_img').append(img_2);
	  }
 });

  $( 'button#submit_demo' ).on('click', function(event)
  {
     event.preventDefault(); // Prevent form from being submitted
     console.log('test');
     var data = new FormData($('form#postarea').get(0));
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
		  $('#category_name_1').remove();
		  $('#category_name_2').remove();
		  $('#description_2').remove();
		  $('#description_1').remove();
		  c1_name = '<h1 class="display-4 font-italic" id="category_name_1">'+data['name_1']+'</h1>';
          c1_des = '<p class="lead my-3" style="color: white" id="description_2">' + data['description_1'] + '</p>'
		  $('#c1_container').prepend(c1_des);
		  $('#c1_container').prepend(c1_name);
		  c2_name = '<h1 class="display-4 font-italic" id="category_name_2">'+data['name_2']+'</h1>';
          c2_des = '<p class="lead my-3" style="color: white" id="description_2">' + data['description_2'] + '</p>'
		  $('#c2_container').prepend(c2_des);
		  $('#c2_container').prepend(c2_name);

		  $('div#c1_container_img').empty();
		  $('div#c2_container_img').empty();
		  img_1 = '<img src=/storey/demo_picture_1/' + data['username'] + '? class="inline-block" width="200" height="200">'
		  $('div#c1_container_img').append(img_1);
		  img_2 = '<img src=/storey/demo_picture_2/' + data['username'] + ' class="inline-block" width="200" height="200">'
		  $('div#c2_container_img').append(img_2);

      }
	 });

    });


  $('#postarea').on('submit', function(event) {
      event.preventDefault(); // Prevent form from being submitted
    });

}); 
