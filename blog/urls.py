from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/
    path('', views.postList, name='list'),
    # ex: /blog/#/
    path('<int:post_id>/', views.singlePost, name='single'),
    # ex: /blog/first/
    path('first/', views.first, name='first'),
    # ex: /blog/random/
    path('random/', views.randomPost, name='random'),
    # ex: /blog/search/
    path('search/', views.search, name='search'),
    # ex: /blog/addpost/
    path('addpost/', views.addpost, name='addpost'),
]