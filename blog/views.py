from datetime import date, datetime
from email.policy import HTTP
import site
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
import calendar


def getArchivesList():
    latest_post_list = Post.objects.order_by('pub_date')
    archivesList = []

    month_yyyy = {}
    last_label = "XXX"
    for p in latest_post_list:
        month_yyyy['label'] = calendar.month_name[p.pub_date.month] + \
            " " + str(p.pub_date.year)
        month_yyyy['href'] = "/" + \
            str(p.pub_date.year) + "/" + str(p.pub_date.month)
        if last_label != month_yyyy['label']:
            archivesList.append(month_yyyy)
            last_label = month_yyyy['label']
        month_yyyy = {}
    return archivesList


sitewide = {
    'about': aboutme.about,
    'media_url': settings.MEDIA_URL,
    'media_heading': 'https://',
    'archivesList': getArchivesList(),
    'header_title': 'griffinsteffy.com'
}

if(settings.REMOTE_SERVER) is False:
    sitewide['media_heading'] = ''


def first(request):
    oldest_posts = Post.objects.order_by('pub_date')
    return redirect('/blog/%s/' % oldest_posts[0].id)


def randomPost(request):
    posts = Post.objects.all()
    rndm = getRandNum(len(posts))
    redirect_str = str('/blog/%s/' % posts[rndm].id)
    return redirect(redirect_str)


def recentPostList(request):
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
            'total_posts': len(latest_post_list),
            'latest_post_list': latest_post_list[:5],
            'featured_post': featured_post,
            'featured_post_id': feature_post_id,
            'weeks_past': weeks_past(aboutme.about['start_date']),
            'sitewide': sitewide
        }
    else:
        context = sitewide
    return render(request, 'blog/recent_list.html', context)


def allPostsList(request):
    post_list = Post.objects.order_by('-pub_date')
    if(post_list.count() > 0):
        featured_post = post_list[0]
        feature_post_id = -1
        for p in post_list:
            if p.is_featured:
                featured_post = p
                feature_post_id = featured_post.id
                break
        # post_list.exclude(id=featured_post.id)
        context = {
            'post_list': post_list,
            'featured_post': featured_post,
            'featured_post_id': feature_post_id,
            'weeks_past': weeks_past(aboutme.about['start_date']),
            'sitewide': sitewide
        }
    else:
        context = sitewide
    return render(request, 'blog/archive_list.html', context)


def postId(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    print('/blog/'+post.slug)
    return HttpResponseRedirect('/blog/'+post.slug)


def singlePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_id = post.pk
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
                    next_pk = latest_post_list[index-1].pk

                if index < post_list_size - 1:
                    prev_pk = latest_post_list[index+1].pk
                break
            index += 1

    hit_count = HitCount.objects.get_for_object(post)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    content = str(post.content)

    file_exists = exists('media/'+str(post.content))
    if(not(file_exists)):
        url = 'https://' + os.getenv("AWS_S3_CUSTOM_DOMAIN",
                                     settings.LOCAL_AWS_S3_CUSTOM_DOMAIN) + '/media/' + content
        savePage(url, 'media/'+str(post.content))

    context = {
        'post': post,
        'sitewide': sitewide,
        'next_pk': str(next_pk),
        'prev_pk': str(prev_pk),
        'header_title': post.title,
        'header_subtitle': post.preview,
        'meta_description': post.featured_preview
    }

    return render(request, content, context)


def archives(request, yyyy, mm):
    archive_posts_list = Post.objects.filter(
        Q(pub_date__year=yyyy) & Q(pub_date__month=mm)).distinct()
    if archive_posts_list.count() > 0:
        context = {
            'archive_selection': datetime(yyyy, mm, 1),
            'post_list': archive_posts_list,
            'sitewide': sitewide
        }
        return render(request, 'blog/archive_list.html', context)
    return allPostsList(request)


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
            sitewide['archivesList'] = getArchivesList()
        else:
            print("form not valid")
    return HttpResponseRedirect("/")
