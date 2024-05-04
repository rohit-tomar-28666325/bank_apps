from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .viewsModules.login import LoginView
from .viewsModules.signup import SignUpView
from .viewsModules.otp import OTPView
from .viewsModules.dashboard import DashboardView
from .viewsModules.transaction import TransactionView
from .viewsModules.setting import SettingView



urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('signup1/', SignUpView.as_view(), name = 'signup1'),
    path('signup2/', SignUpView.as_view(), name = 'signup2'),
    path('signup3/', SignUpView.as_view(), name = 'signup3'),
    path('signup4/', SignUpView.as_view(), name = 'signup4'),
    path('otp/', OTPView.as_view(), name = 'otp'),
    path('main/', DashboardView.as_view(), name = 'main'),
    path('card/', views.card, name = 'card'),
    path('settings/', SettingView.as_view(), name = 'settings'),
    path('loan/', views.loan, name = 'loan'),
    path('help/', views.help, name = 'help'),
    path('investment/', views.investment, name = 'investment'),
    path('transaction/', TransactionView.as_view(), name = 'transaction'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
