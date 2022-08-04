from django.urls import path

from . import views

urlpatterns = [
    # ex: /category/
    path('', views.link, name='link'),
    path('test/', views.testing, name='testing'),
    
    # plaid api
    # path('create_link_token', views.create_link_token, name='create_link_token'),

]