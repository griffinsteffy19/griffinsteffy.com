from email.policy import HTTP
from random import randrange
from turtle import pos
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random
from .models import Post

def getRandNum(range):
    return random.randrange(0, range)

def first(request):
    posts = Post.objects.all()
    return redirect('/blog/%s/' % posts[0].id)

def randomPost(request):
    posts = Post.objects.all()
    print(len(posts))
    rndm = getRandNum(len(posts))
    print(rndm)
    redirect_str = str('/blog/%s/' % posts[rndm].id)
    return redirect(redirect_str)

def postList(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    print (type (latest_post_list))
    featured_post = latest_post_list[0]
    found_featured = False
    for p in latest_post_list:
        if p.is_featured:
            featured_post = p
            break
    latest_post_list.exclude(id=featured_post.id)
                    
    context = {
        'latest_post_list': latest_post_list,
        'featured_post' : featured_post,
        'featured_post_id': featured_post.id
    }
    return render(request, 'blog/list.html', context)

def singlePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    content = str(post.content)
    find_str = 'templates'
    start = content.find(find_str, 1, len(content)) + len(find_str)+1
    return render(request, str(post.content)[start:], {'post': post})

def test(request):
    return render(request, 'blog/blog_template.html')