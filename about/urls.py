from django.urls import path

from . import views

urlpatterns = [
    # ex: about/
    path('', views.about, name='about'),
    # ex: /about/resume/
    path('resume/', views.resume, name='resume'),
    # ex: /about/resume/
    path('contact/', views.contact, name='contact'),
]