from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'front/home.html')

def about(request):
    return render(request, 'front/about.html')

def contact(request):
    return render(request, 'front/contact.html')

def projects(request):
    return render(request, 'front/projects.html')

def registration(request):
    return render(request, 'front/registration.html')