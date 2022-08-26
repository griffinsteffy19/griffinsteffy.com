from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    path('', views.recentPostList, name='recentPostList'),
    # ex: /blog/all.
    path('all/', views.allPostsList, name='allPostsList'),
    # ex: /blog/#/
    path('<int:post_id>/', views.postId, name='postId'),
    # ex: /blog/<slug>/
    path("<slug:slug>",  views.singlePost, name='single'),
    # ex: /blog/first/
    path('first/', views.first, name='first'),
    # ex: /blog/random/
    path('random/', views.randomPost, name='random'),
    # ex: /blog/search/
    path('search/', views.search, name='search'),
    # ex: /blog/addpost/
    path('addpost/', views.addpost, name='addpost'),
    # ex: /blog/<yyyy>/<mm>
    path("<int:yyyy>/<int:mm>",  views.archives, name='archives'),
]