from django.test import TestCase, Client
from django.urls import reverse
from website.models.models import Customers 
from website.views import CustomersForm, TransactionForm

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Add any necessary setup code here, such as creating test data

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    # Add similar test methods for other views...

    def test_login_view(self):
        # Assuming you have setup test data for MainCustomers
        email = "test@example.com"
        password = "testpassword"
        Customers.objects.create(email=email, password=password, status="Active")
        
        # Test login with correct credentials
        response = self.client.post(reverse('login'), {'email': email, 'password': password})
        self.assertEqual(response.status_code, 200)  # Redirects to OTP view on successful login

        # Test login with incorrect credentials
        response = self.client.post(reverse('login'), {'email': email, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid password')
