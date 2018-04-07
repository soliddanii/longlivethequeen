$( document ).ready(function() {

    var viewportWidth = $("body").innerWidth();
    var viewportHeight = $("body").innerHeight();

    if(viewportWidth>700 && viewportHeight>500)
    {

        // Fade in the elodie image
        $("#elodie").animate({
            left: "0px",
            opacity: 1
        }, 1500, function() {
            // Animation complete.
            $(".wrapper").css("overflow", "auto");
        });

    }
    else
    {
        $(".wrapper").css("overflow", "auto");
    }
    
});