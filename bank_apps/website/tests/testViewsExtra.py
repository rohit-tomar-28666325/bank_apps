from django.test import SimpleTestCase, Client
from django.urls import reverse
from website.testets_models import Customers, Transaction
from datetime import datetime, timedelta
import json
from website.views import formOTP, send_otp



class TestViews(SimpleTestCase):
    databases = ['default']

    def setUp(self):
        self.client = Client()
        self.customer = Customers.objects.create(
            email='test@example.com',
            password='test_password',
            status='Active',
            last_name='TestLast'
        )

    def test_login_post_request(self):
        url = reverse('login')  # Assuming your login URL name is 'login'
        data = {
            'email': 'test@example.com',
            'password': 'test_password'
        }

        # Perform POST request
        response = self.client.post(url, data)

        # Check if the response status code is as expected
        self.assertEquals(response.status_code, 302)  # Assuming you're redirecting after successful login

        # Check if the user is redirected to the correct URL (replace 'otp' with your redirect URL)
        self.assertRedirects(response, reverse('otp'))

        # Check if session variables are set correctly
        self.assertEquals(self.client.session['username'], 'TestLast')
        self.assertEquals(self.client.session['email'], 'test@example.com')

    def test_login_invalid_credentials(self):
        url = reverse('login')
        data = {
            'email': 'invalid@example.com',
            'password': 'invalid_password'
        }

        response = self.client.post(url, data)

        # Check if the response status code is as expected (rendering login page)
        self.assertEqual(response.status_code, 200)

        # Check if the error message is displayed
        self.assertContains(response, 'Invalid email ID. Please enter valid Email ID')

    def test_login_invalid_password(self):
        url = reverse('login')
        data = {
            'email': 'test@example.com',
            'password': 'invalid_password'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid password. Please enter correct password')

    def test_signup1_post_request(self):
        url = reverse('signup1')  # Assuming your signup1 URL name is 'signup1'

        # Test with valid POST data
        data_valid = {
            'actionBtn': 'Proceed'
            # Add other required fields here
        }
        response_valid = self.client.post(url, data_valid)
        self.assertEqual(response_valid.status_code, 302)  # Redirect after successful form submission
        self.assertRedirects(response_valid, reverse('signup2'))
        self.assertEqual(self.client.session['tempData1'], data_valid)

        # Test with invalid POST data
        data_invalid = {
            'actionBtn': 'InvalidAction'
            # Add other required fields here
        }
        response_invalid = self.client.post(url, data_invalid)
        self.assertEqual(response_invalid.status_code, 200)  # Rendering the same page after invalid form submission
        # Add assertion for any error message or expected behavior in case of invalid data

    def test_signup2_post_request(self):
        url = reverse('signup2')  # Assuming your signup2 URL name is 'signup2'

        # Test with valid POST data
        data_valid = {
            'actionBtn': 'Proceed'
            # Add other required fields here
        }
        response_valid = self.client.post(url, data_valid)
        self.assertEqual(response_valid.status_code, 302)  # Redirect after successful form submission
        self.assertRedirects(response_valid, reverse('signup3'))
        self.assertEqual(self.client.session['tempData2'], data_valid)

        # Test with invalid POST data
        data_invalid = {
            'actionBtn': 'InvalidAction'
            # Add other required fields here
        }
        response_invalid = self.client.post(url, data_invalid)
        self.assertEqual(response_invalid.status_code, 200)  # Redirecting to signup1
        self.assertRedirects(response_invalid, reverse('signup1'))


    def test_signup3_post_request(self):
        url = reverse('signup3')  

        data_valid = {
            'actionBtn': 'Proceed'
        }
        response_valid = self.client.post(url, data_valid)
        self.assertEqual(response_valid.status_code, 302)  
        self.assertRedirects(response_valid, reverse('signup4'))
        self.assertEqual(self.client.session['tempData3'], data_valid)

        data_invalid = {
            'actionBtn': 'InvalidAction'
        }

        response_invalid = self.client.post(url, data_invalid)
        self.assertEqual(response_invalid.status_code, 200) 
        self.assertRedirects(response_invalid, reverse('signup2'))

    # def test_signup4_post_proceed(self):

        # Set up session data
        # session = self.client.session
        # session['tempData1'] = {'last_name': 'Doe'}  # Sample data
        # session['tempData2'] = {'email': 'test@example.com'}  # Sample data
        # session.save()

        # POST request with actionBtn as 'Proceed'
        # response = self.client.post(reverse('signup4'), {'actionBtn': 'Proceed'}, follow=True)

        # Check if the session data is set correctly
        # self.assertEqual(response.status_code, 302)  # Should redirect to 'otp'
        # self.assertEqual(response.redirect_chain[0][0], reverse('otp'))
        # self.assertIn('email', self.client.session)  # Check if email is stored in session
        # self.assertEqual(self.client.session['email'], 'test@example.com')

    # def test_signup4_post_not_proceed(self):
        # Set up session data
        # session = self.client.session
        # session['tempData1'] = {'last_name': 'Doe'}  # Sample data
        # session['tempData2'] = {'email': 'test@example.com'}  # Sample data
        # session.save()

        # POST request with actionBtn not 'Proceed'
        # response = self.client.post(reverse('signup4'), {'actionBtn': 'Cancel'}, follow=True)

        # Check if redirected to signup3
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.redirect_chain[0][0], reverse('signup3'))

    # def test_card_post_proceed(self):
        # POST request with actionBtn as 'Proceed'
        # response = self.client.post(reverse('card'), {'actionBtn': 'Proceed'}, follow=True)

        # Check if redirected to 'dashboard'
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.redirect_chain[0][0], reverse('dashboard'))

    # def test_card_post_not_proceed(self):
        # POST request with actionBtn not 'Proceed'
        # response = self.client.post(reverse('card'), {'actionBtn': 'Cancel'}, follow=True)

        # Check if still on the same page
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'card.html')