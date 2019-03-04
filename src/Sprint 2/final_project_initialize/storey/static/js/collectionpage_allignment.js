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

  $('#allignmentform').on('submit', function(event) {
     
    event.preventDefault(); // Prevent form from being submitted
      $("img#preview").remove();
      var form = $('#allignmentform').serializeArray();
      var paras = {}

      $('#allignmentform :input').each(function () {
        if ($(this).is(":checkbox")) {
          paras[$(this).attr('name')] = $(this).is(':checked') ? 'on' : ''
        } else {
          paras[$(this).attr('name')] = $(this).val(); 
        }
      });

      $.post('/storey/editCollectionpageAllignment/', paras)
        .done(function(data) {
          updateAllignmentChanges(data);
});
  });

  function makePaging(totalPages, pageIndex) {
    var oPaging, i, j, k;
    var totalPages = parseInt(totalPages);

    pageIndex++;

    i = pageIndex;
    j = pageIndex - 1;
    k = pageIndex + 1;

    var oBefore, oAfter;
    oBefore = "";
    oAfter = "";

    while (j != 0 && j != i - 6) {
        oBefore = "<a class='Page' href='#' data-index='" + (j - 1) + "'>" + j + "</a>&nbsp;" + oBefore;
        j--;
    }

    for (; k < totalPages + 1 && k < i + 6; k++) {
        oAfter += "<a class='Page' href='#' data-index='" + (k - 1) + "'>" + k + "</a>&nbsp;";
    }

    oPaging = oBefore + "<a class='CurPage' href='#' rel='' style='color:Red;'>" + i.toString() + "</a>&nbsp;" + oAfter;

    return oPaging;
}


  // The following function will help you update the contents of the
  // page based on our application's JSON response.
  function updateAllignmentChanges(data) {
    var sorting_content = document.getElementById("sorting_content");
    while (sorting_content.childElementCount > 0) {
      sorting_content.removeChild(sorting_content.lastChild);
    }
    if (data['allignment_sorting']) {
      $("#sorting_content").append($("#sorting_template").html());
    }

    var content = document.getElementById("collection_content");
    while (content.childElementCount > 0) {
      content.removeChild(content.lastChild);
    }
    for (var i = 0; i < data['allignment_row']; i++) {
        $("#collection_content").append($("#row_template").html());
    }

    var numberperpage = data['allignment_row'] * 4;
    var totalPages = 100 / numberperpage + 1;
    var pagination = makePaging(totalPages, 1)
    var child = document.createElement('div');
    child.innerHTML = pagination;
    var pages = document.getElementById("collection_pagination");
    if (pages.childElementCount > 0) {
      pages.removeChild(pages.lastChild);
    }
    pages.appendChild(child);
  }

}); // End of $(document).ready