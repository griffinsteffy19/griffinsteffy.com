from email.policy import HTTP
from multiprocessing import context
from random import randrange
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import random
from .models import Post
from django.db.models import Q
from .forms import NewPostForm
from griffinsteffy import settings

from about import aboutme

sitewide = {
    'about': aboutme.about
}

def getRandNum(range):
    return random.randrange(0, range)

def first(request):
    posts = Post.objects.all()
    return redirect('/blog/%s/' % posts[0].id)

def randomPost(request):
    posts = Post.objects.all()
    rndm = getRandNum(len(posts))
    redirect_str = str('/blog/%s/' % posts[rndm].id)
    return redirect(redirect_str)

def postList(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    if(latest_post_list.count() > 0):
        featured_post = latest_post_list[0]
        feature_post_id = -1
        found_featured = False
        for p in latest_post_list:
            if p.is_featured:
                featured_post = p
                feature_post_id = featured_post.id
                break
        latest_post_list.exclude(id=featured_post.id)
        context = {
            'latest_post_list': latest_post_list,
            'featured_post' : featured_post,
            'featured_post_id': feature_post_id,
            'media_url': settings.MEDIA_URL,
        }
    else:
        context = sitewide
    return render(request, 'blog/list.html', context)

def singlePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    content = str(post.content)
    context = {
        'post': post,
        'media_url': settings.MEDIA_URL,
        'sitewide': sitewide
    }

    return render(request, content, context)

def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        search_filter = request.GET.get("search_text")
        if search_filter == 'login':
            return HttpResponseRedirect("/accounts/login/")
        search_posts_list = Post.objects.filter(Q(title__contains=search_filter) | Q(tags__slug=search_filter))
        if search_posts_list.count() > 0:
            context = {
                'search_results': search_posts_list, 
                'media_url': settings.MEDIA_URL,
                'sitewide': sitewide
                }
            return render(request, 'blog/search_results.html', context)

    return postList(request)

def addpost(request):
    if request.method == 'GET':
        form = NewPostForm()
        context = {
                'form': form,
                'sitewide': sitewide
                }
        return render(request, 'blog/addpost.html', context)
    else:
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print("form not valid")
    return HttpResponseRedirect("/")
