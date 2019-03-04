
$(document).ready(function($)
{
    var navbarTrans = function()
    {
        if ($("#mainNav").offset().top <= 100)
        {
            $("#mainNav").removeClass("navbar-trans");
        }
        else
        {
            $("#mainNav").addClass("navbar-trans");
        }
    };
    $(window).scroll(navbarTrans);

});