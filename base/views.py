from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
def home(request):
    return HttpResponseRedirect(reverse('blog:home'))