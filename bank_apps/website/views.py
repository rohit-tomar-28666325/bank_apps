from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'login.html', {'title': 'home'})

def about(request):
    return render(request, 'login.html', {'title': 'about'})

def login(request):
    return render(request, 'login.html')

def otp(request):
    return render(request, 'otp.html')
    
def main(request):
    return render(request, 'main.html')
# def signup1(request):
#    return render(request, 'signup1.html')
def signup1(request):
    return render(request, 'signup1.html')

def signup2(request):
    return render(request, 'signup2.html')

def signup3(request):
    return render(request, 'signup3.html')

def signup4(request):
    return render(request, 'signup4.html')




