$(document).ready(function () {

    // $(body).css('minheight',$(window).height());
    //nav event
    $('.nav-item').click(function () {
        if (!$(this).hasClass('nav-active')) {
            $(this).children('.nav-link').addClass('nav-active');
            $(this).siblings().children('.nav-link').removeClass('nav-active');
        } else {
            return;
        }
    });

    //rotate event&drop down list event
    $('.arrow-r').click(function () {
        if ($(this).children().hasClass("rotate-0")) {
            $(this).children().addClass("rotate-180").removeClass("rotate-0");
            $('.dropdown-list').fadeIn(300).show();
        } else {
            $(this).children().addClass("rotate-0").removeClass("rotate-180");
            $('.dropdown-list').fadeOut(300).hide();
        }
    });

    $('.dropdown-single').click(function () {
        if ($(event.target).is("input"))
            return;
            console.log($(this).text());
        $('.arrow-l').val($(this).text());
        $('.arrow-img').removeClass('rotate-180').addClass('rotate-0');
        $('.dropdown-list').fadeOut(300).hide();
    });

    //identity option evnet
    $('.identity-option').click(function () {
        if ($(event.target).is("input"))
            return;
        if ($(this).hasClass('high-light')) {
            return;
            // $(this).removeClass('high-light');
        } else {
            $(this).addClass('high-light').siblings().removeClass('high-light');
        }
    });

});