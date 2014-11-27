$(function() {
    $(document).on('click','.flip',flip_form);
    //$(window).on("scroll", get_more_post);
    if(window.SIGN_UP) flip_form();    
    $('.m-comment').autosize();
    $('.new-comment').autosize();
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

$('textarea#content').keypress(function(e) {
    if(e.keyCode == 13 || e.which == 13) {
        jQuery(this).blur();
        jQuery('#post-new').click();
    }
});


$('textarea.m-comment').keypress(function(e) {
    if((e.keyCode == 13 || e.which == 13) && $(this).val() != "" ){
        var content = $(this).val(),
        post_id = $(this).data("post-id");
        $(this).val("");
        var data = {
            "content": content,
            "post_id": post_id,
        }
        $.ajax({
            url: '/create-comment/',
            type: 'POST',
            data: data,
        })
        .done(function(data) {        
            $("#"+post_id).append(data);
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
        });
        
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
    }
}
 