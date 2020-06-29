$(document).ready(function () {

    $('body').css('height', window.screen.height);
    console.log(window.screen.height);

    $('.arrow-img').on('click', function () {
        let class_name = 'arrow-rotate';
        if ($(this).hasClass(class_name)) {
            $('.td-nav').show(300);
            $(this).removeClass(class_name);
            // $('.td-content').css('width','70%');
        } else {
            $('.td-nav').hide(300);
            $(this).addClass(class_name);
            // $('.td-content').css('width','95%');
        }
    })

    $('.nav-a').on('click', function () {
        let class_name = 'nav-a-active';
        if (!$(this).hasClass(class_name)) {
            $(this).addClass(class_name);
            $(this).parents().siblings().children().removeClass(class_name);
        }
    })

    $('.sub-nav-a').on('click', function () {
        // $(this).removeClass('active');
        let class_name = 'sub-nav-a-active';
        if (!$(this).hasClass(class_name)) {
            $(this).addClass(class_name);
            $(this).parents().siblings().children().removeClass(class_name);
            let href = $(this).attr('href');
            // console.log('href=' + href);
            let src = $(href).attr('src');
            // console.log('src=' + src);
            convertImageToCanvas(src);
        }
    })

    $('.button-save').on('click', function () {
        let imgUrl = '';
        let newImgUrl = convertCanvasToImage(imgUrl);
        $('.img-url').text(newImgUrl);
    })

    // var color = "#" + $("#color").val();
    // var width=$("#penWidth option:selected").text();
    // $('.button-draw').on('click', CanvasExt.drawPen("can", color));

    // 将图片存入canvas
    function convertImageToCanvas(image) {
        $('.can').width = image.width;
        $('.can').height = image.height;
        image.onload = function () {
            $('.can').getContext("2d").drawImage(image, 0, 0);
            return canvas;
        }
    }

    // 将canvas存为图片
    function convertCanvasToImage(imgUrl) {
        var image = new Image();
        image.src = $('.can').toDataURL(imgUrl);
        return image;
    }
})