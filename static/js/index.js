$(function() {
    //$(window).on("scroll", get_more_post);
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
            .html('<i class="fa fa-spinner fa-spin loading"></i>' + btn.html()).addClass("text-center")
    }
}


function get_more_post(){
    var scrollAmount = $(window).scrollTop(),
    documentHeight = $(document).height(),
    content = $(window).height();
    if(scrollAmount == (documentHeight - content)) {
    }
}
 
$(document).on("click",".viewmore-comment",function(e) {
    var $ele = $(this);
    loading($ele)
    var page = $(this).data("page"),
    post_id = $(this).data("post-id");
    var data = {
        "page": page,
        "post_id": post_id,
    }
    $.ajax({
        url: '/get-comment/',
        type: 'POST',
        data: data,
    })
    .done(function(data) {        
        $("#"+post_id).prepend(data);
    })
    .fail(function() {
        console.log("error");
    })
    .always(function() {
        $ele.remove();
    });
        
});