$(function () {
    $(".screen-height").height($(window).height());

    $(window).resize(function () {
        $(".screen-height").height($(window).height());
    });

    $(".start-stop").click(function () {
        $('.jumbotron__inner-item p').removeClass('animation-true').eq($(this).index()).addClass("animation-true");
        $("button").removeClass("active").eq($(this).index()).addClass("active");
    });
    $(".pause-button").click(function () {
        $('.jumbotron__inner-item p').toggleClass('animation-true');
        $(".pause-button").toggleClass('active');
        
    });
    $("#next").click(function () {
        $(".result__box").fadeOut(200)
        $(".jumbotron__inner").fadeIn(200)

    });
    $("#stop").click(function () {
        // $('#quest').load(document.URL + ' #quest');
        $(".jumbotron__inner").fadeOut(200)
        $(".result__box").fadeIn(200)
        
    });
});

