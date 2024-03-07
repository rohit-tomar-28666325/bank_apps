from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'home.html', {'title': 'home'})

def about(request):
    return render(request, 'about.html', {'title': 'about'})

def login(request):
    return render(request, 'login.html')

# def signup1(request):
#    return render(request, 'signup1.html')


