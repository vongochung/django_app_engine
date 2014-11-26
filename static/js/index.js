$(function() {
    $(document).on('click','.flip',flip_form);
    //$(window).on("scroll", get_more_post);
    if(window.SIGN_UP) flip_form();    
    $('.m-comment').autosize();
    $('.m-comment').css({"lin-height": "2px!important" }).trigger('autosize.resizeIncludeStyle'); 

});

$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                     break;
                 }
             }
         }
         return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

function loading(btn)
{
    var loading = btn.find('.loading').length
    if (loading) {
        btn.find('.loading').remove()
    } else {
        btn
            .html('<i class="fa fa-spinner fa-spin fa-2x loading"></i>' + btn.html()).addClass("text-center")
    }
}

function isIE(){
    if (navigator.appName == 'Microsoft Internet Explorer')
        return true
    return false
}

function flip_form()
{
   if (Modernizr.csstransforms3d && !isIE()) {
        $('.card').toggleClass('flipping');
   } else {
        var page = $(this).closest('.face'),
        front = $('.front'),
        back = $('.back');
        if ( page.hasClass('front')) {
            front.toggleClass('front').addClass('back');
            back.toggleClass('back').addClass('front');

        } else{
            back.toggleClass('back').addClass('front');
            front.toggleClass('front').addClass('back');
        }
       
    }
}

$(document).on("click", "#btn-regist" ,function(){    
    loading($(this));
    var data = {
        "email" : $("#form-signup #email").val(),
        "password": $("#form-signup #id_password").val(),
        "re_password": $("#form-signup #id_re_password").val(),
        "captcha_1": $("#form-signup #id_captcha_1").val(),
        "captcha_0": $("#form-signup #id_captcha_0").val()
    }
    $.ajax({
        type: 'POST' ,
        url: '/signup',
        async: true,
        data: data,
        success: function(data) {
            $('#form-signup').html(data);
        }
    });
    return false;
});


function get_more_post(){
    var scrollAmount = $(window).scrollTop(),
    documentHeight = $(document).height(),
    content = $(window).height();
    if(scrollAmount == (documentHeight - content)) {
        $(".content").append('<div class="col-md-7 col-sm-6 col-xs-6 post">'+
                '<div class="header-post">'+
                    '<a href="#">'+
                        '<div class="head-img">'+
                            '<img class="profile-img small img-circle " src="http://www.gravatar.com/avatar/00000000000000000000000000000000?d=mm&amp;f=y">'+
                        '</div>'+
                        '<span class="head-name">Võ Ngọc Hưng</span>'+
                    '</a>'+
                '</div>'+
                '<div class="title-post"> Title của bài post Title của bài post Title của bài post Title của bài post Title của bài post</div>'+
                '<a href="#">'+
                    '<img class="img-responsive" src="/static/uploads/test2.png">'+
                '</a>'+
                '<div class="footer-post">'+
                    '<a href="#">Thích</a>'+
                    '<a href="#">Bình luận</a>'+
                    '<a href="#">Chia sẽ</a>'+
                '</div>'+
            '</div>'
        );
    }
}
 