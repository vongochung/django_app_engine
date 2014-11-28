# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.http import Http404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from home.models import POST,COMMENT
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger

now = datetime.now()
@login_required(login_url='/accounts/login/')
def index(request):
	posts = POST.objects.all().order_by('-date')[:10]
	return render_to_response('home/index.html', {"posts":posts}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def create_post(request):
	if request.method == 'POST':
		post = POST()
        post.content = request.POST.get('content')
        post.author = request.user
        post.date = now
        post.save()
	return HttpResponseRedirect('/')

@login_required(login_url='/accounts/login/')
def create_comment(request):
	if request.method == 'POST':
		comment = COMMENT()
        comment.content = request.POST.get('content')
        comment.author = request.user
        comment.post_id =  request.POST.get('post_id')
        comment.date = now
        comment.save()

        return render_to_response("comment/one_comment.html",{ "comment":comment }, context_instance=RequestContext(request))
	
	return HttpResponse(status=400)


@login_required(login_url='/accounts/login/')
def get_comment(request):
	if request.method == 'POST':
		postID=request.POST.get('post_id')
		comments_list = COMMENT.objects.filter(post_id=postID).order_by("-date")
		paginator = Paginator(comments_list, 5)
		page = request.POST.get('page')
		try:
			comments = paginator.page(page)
		except PageNotAnInteger:
			return HttpResponse(status=400)

		return render_to_response('comment/comment_ajax.html',
			{
				"comments": reversed(comments),
				"post_id":postID,
				"hasnext":comments.has_next(),
				"next_page":comments.next_page_number(),
			},  context_instance=RequestContext(request))
	
	return HttpResponse(status=400)