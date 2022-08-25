from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about/about.html')

def contact(request):
    return render(request, 'about/contact.html')

def resume(request):
    context = {}
    return render(request, 'about/resume.html', context)