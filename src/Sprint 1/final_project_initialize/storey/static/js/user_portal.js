$(document).ready(function(){
var $B = $('body'),
    $SIDEBAR = $('#sidebar-menu');
 $SIDEBAR.find('a').on('click', function(ev) {
        var $li = $(this).parent();
        if ($li.is('.active'))
        {
            $li.removeClass('active active-sm');
            $('ul:first', $li).slideUp(function() {
                setContentHeight();
            });
        }
        else
        {
            if ($li.parent().is('.child_menu'))
            {
                if ( $B.is( ".nav-sm" ) )
                {
                    $li.parent().find( "li" ).removeClass( "active active-sm" );
                    $li.parent().find( "li ul" ).slideUp();
                }
            }
            else
            {
                $SIDEBAR.find('li').removeClass('active active-sm');
                $SIDEBAR.find('li ul').slideUp();
            }
            $li.addClass('active');

            $('ul:first', $li).slideDown(function()
            {
                setContentHeight();
            });
        }
    });
});
 // TODO: on click erase the child menu