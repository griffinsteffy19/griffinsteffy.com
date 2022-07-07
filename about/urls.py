from django.urls import path

from . import views

urlpatterns = [
    # ex: /about/resume/
    path('resume/', views.resume, name='resume'),
]