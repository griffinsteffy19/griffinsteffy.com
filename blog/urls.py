from django.urls import path

from . import views

urlpatterns = [
    # ex: /blog/list/
    path('', views.postList, name='list'),
    # ex: /blog/5/
    path('<int:post_id>/', views.singlePost, name='single'),
    # ex: /blog/first/
    path('first/', views.first, name='first'),
    # ex: /blog/random/
    path('random/', views.randomPost, name='random'),
    # ex: /blog/test/
    path('test/', views.test, name='test'),
]