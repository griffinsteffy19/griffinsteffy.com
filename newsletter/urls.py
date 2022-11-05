from django.urls import path
from . import views

app_name = "newsletter"

urlpatterns = [
    # ex: /newsletter/
    path('', views.subscribeForm, name='subscribeForm'),
    # ex: /newsletter/subscribe/
    path('subscribe/', views.subscribe, name='subscribe'),
]