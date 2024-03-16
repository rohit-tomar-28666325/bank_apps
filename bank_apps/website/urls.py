from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('login/', views.login, name = 'login'),
    path('otp/', views.otp, name = 'otp'),
    # path('signup1/', views.signup1, name = 'signup1'),
]