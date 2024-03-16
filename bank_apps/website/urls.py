from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('login/', views.login, name = 'login'),
    path('otp/', views.otp, name = 'otp'),
    path('main/', views.main, name = 'main'),
    # path('signup1/', views.signup1, name = 'signup1'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
