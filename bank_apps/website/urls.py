from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name = 'home'),
    # path('about/', views.about, name = 'about'),
    
    path('', views.login, name = 'login'),
    path('signup1/', views.signup1, name = 'signup1'),
    path('signup2/', views.signup2, name = 'signup2'),
    path('signup3/', views.signup3, name = 'signup3'),
    path('signup4/', views.signup4, name = 'signup4'),
    path('otp/', views.otp, name = 'otp'),
    path('main/', views.main, name = 'main'),
    path('card/', views.card, name = 'card'),
    path('settings/', views.setting, name = 'settings'),
    path('loan/', views.loan, name = 'loan'),
    path('help/', views.help, name = 'help'),
    path('investment/', views.investment, name = 'investment'),
    path('transaction/', views.transaction, name = 'transaction'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
