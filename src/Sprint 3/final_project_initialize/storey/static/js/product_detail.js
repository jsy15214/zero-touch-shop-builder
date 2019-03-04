   $(document).ready(function() {
            //-- Click on detail
            $("ul.menu-items > li").on("click",function(){
                $("ul.menu-items > li").removeClass("active");
                $(this).addClass("active");
            })

            $(".attr,.attr2").on("click",function(){
                var clase = $(this).attr("class");

                $("." + clase).removeClass("active");
                $(this).addClass("active");
            })

            //-- Click on QUANTITY
            $(".btn-minus").on("click",function(){
                var now = $(".section > div > input").val();
                if ($.isNumeric(now)){
                    if (parseInt(now) -1 > 0){ now--;}
                    $(".section > div > input").val(now);
                }else{
                    $(".section > div > input").val("1");
                }
            })            
            $(".btn-plus").on("click",function(){
                var now = $(".section > div > input").val();
                if ($.isNumeric(now)){
                    $(".section > div > input").val(parseInt(now)+1);
                }else{
                    $(".section > div > input").val("1");
                }
            }) 


            $('#detailform').on('submit', function(event) {
     
    event.preventDefault(); // Prevent form from being submitted
    
      var form = $('#detailform').serializeArray();
      var paras = {}

      $('#detailform :input').each(function () {
        if ($(this).is(":checkbox")) {
          paras[$(this).attr('name')] = $(this).is(':checked') ? 'on' : ''
        } else {
          paras[$(this).attr('name')] = $(this).val();
      }
      });

      $.post('/storey/editCollectionpageDetail/', paras)
        .done(function(data) {
          updateDetailChanges(data);
});
  });

    // The following function will help you update the contents of the
  // page based on our application's JSON response.
  function updateDetailChanges(data) {
    var content = document.getElementById("product_comments");
    while (content.childElementCount > 0) {
      content.removeChild(content.lastChild);
    }


    var child = document.createElement('div');
    child.innerHTML = '<h1>Comments: </h1>';
    if (data['detail_commenting']) {
        content.append(child); 
    }
    }                 
        });