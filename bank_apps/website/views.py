from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'login.html', {'title': 'home'})

def about(request):
    return render(request, 'login.html', {'title': 'about'})

def login(request):
    return render(request, 'login.html')

def otp(request):
    return render(request, 'otp.html')

# def signup1(request):
#    return render(request, 'signup1.html')

