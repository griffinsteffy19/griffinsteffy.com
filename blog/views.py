from email.policy import HTTP
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post
from django.db.models import Q
from .forms import NewPostForm
import os
from os.path import exists
from griffinsteffy import settings
from about import aboutme

from .functions import getRandNum, weeks_past, savePage

from hitcount.models import HitCount
from hitcount.views import HitCountMixin

sitewide = {
    'about': aboutme.about,
    'media_url': settings.MEDIA_URL,
}


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
        for p in latest_post_list:
            if p.is_featured:
                featured_post = p
                feature_post_id = featured_post.id
                break
        latest_post_list.exclude(id=featured_post.id)
        context = {
            'latest_post_list': latest_post_list,
            'featured_post': featured_post,
            'featured_post_id': feature_post_id,
            'weeks_past': weeks_past(aboutme.about['start_date']),
            'sitewide': sitewide
        }
    else:
        context = sitewide
    return render(request, 'blog/list.html', context)


def singlePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    latest_post_list = Post.objects.order_by('-pub_date')
    post_list_size = latest_post_list.count()

    is_first = False
    prev_pk = -1
    next_pk = -1
    if(post_list_size > 0):
        if(latest_post_list[0].pk == post_id):
            is_first = True

        index = 0
        for p in latest_post_list:
            if p.pk == post_id:
                if index > 0:
                    prev_pk = latest_post_list[index-1].pk
                
                if index < post_list_size - 1:
                    next_pk = latest_post_list[index+1].pk
                break
            index+=1

    hit_count = HitCount.objects.get_for_object(post)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    content = str(post.content)

    file_exists = exists('media/'+str(post.content))
    if(not(file_exists)):
        url = 'https://' + os.getenv("AWS_S3_CUSTOM_DOMAIN", settings.devAWS_S3_CUSTOM_DOMAIN) + '/media/' + content
        print("savePage")
        savePage(url, 'media/'+str(post.content))

    context = {
        'post': post,
        'sitewide': sitewide,
        'next_pk': str(next_pk),
        'prev_pk': str(prev_pk),
    }

    return render(request, content, context)


def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        search_filter = request.GET.get("search_text")
        if search_filter == 'login':
            return HttpResponseRedirect("/accounts/login/")
        search_posts_list = Post.objects.filter(
            Q(title__contains=search_filter) | Q(tags__slug=search_filter)).distinct()
        if search_posts_list.count() > 0:
            context = {
                'search_results': search_posts_list,
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
