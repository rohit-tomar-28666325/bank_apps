from django.test import SimpleTestCase
from django.urls import reverse, resolve
# from website import views
from website.views import login, signup1, signup2, signup3, signup4, otp, main, card, loan, help, investment, transaction
from django.conf import settings
from django.conf.urls.static import static
from website.middleware.auth import login_required, check_If_Already_LogIn

class TestUrls(SimpleTestCase):
    print("hi")

    