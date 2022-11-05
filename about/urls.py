from django.urls import path

from . import views

app_name = "about"

urlpatterns = [
    # ex: about/
    path('', views.about, name='about'),
    # ex: /about/resume/
    path('resume/', views.resume, name='resume'),
    # ex: /about/resume/
    path('contact/', views.contact, name='contact'),
]