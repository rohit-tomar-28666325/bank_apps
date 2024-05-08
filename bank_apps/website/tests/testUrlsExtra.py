from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import login, signup1, signup2, signup3, signup4, otp, main, card, loan, help, investment, transaction



class TestUrls(SimpleTestCase):

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_signup1_url_is_resolved(self):
        url = reverse('signup1')
        self.assertEquals(resolve(url).func, signup1)

    def test_signup2_url_is_resolved(self):
        url = reverse('signup2')
        self.assertEquals(resolve(url).func, signup2)

    def test_signup3_url_is_resolved(self):
        url = reverse('signup3')
        self.assertEquals(resolve(url).func, signup3)

    def test_signup4_url_is_resolved(self):
        url = reverse('signup4')
        self.assertEquals(resolve(url).func, signup4)

    def test_otp_url_is_resolved(self):
        url = reverse('otp')
        self.assertEquals(resolve(url).func, otp)

    def test_main_url_is_resolved(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func, main)

    def test_card_url_is_resolved(self):
        url = reverse('card')
        self.assertEquals(resolve(url).func, card)

    def test_help_url_is_resolved(self):
        url = reverse('help')
        self.assertEquals(resolve(url).func, help)

    def test_loan_url_is_resolved(self):
        url = reverse('loan')
        self.assertEquals(resolve(url).func, loan)

    def test_investment_url_is_resolved(self):
        url = reverse('investment')
        self.assertEquals(resolve(url).func, investment)

    def test_transaction_url_is_resolved(self):
        url = reverse('transaction')
        self.assertEquals(resolve(url).func, transaction)