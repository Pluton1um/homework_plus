$(document).ready(function () {

    /*main navigation toggle*/
    $("#nav-info,#nav-course").on('click', function () {
        $(".main-nav-a").removeClass("main-nav-active");
        $(this).addClass("main-nav-active");
    });

    /*sub navigation toggle*/
    $("#choice1,#choice2,#choice3,#choice4").click(function () {
        $(".sub-nav-a").removeClass("sub-nav-active");
        $(this).addClass("sub-nav-active");
    });

    /*scroll spy to fix navigation bar*/
    $(document).scroll(function () {
        // var x = $(".navigation-a").offset();
        if ($(window).scrollTop() > 400) {
            $(".navigation-a").addClass("main-nav-fix");
            // $(".left-nav").addClass("sub-nav-fix");
        } else {
            $(".navigation-a").removeClass("main-nav-fix");
            // $(".left-nav").removeClass("sub-nav-fix");
        }
    });

});