from django.views import View
from django.shortcuts import render, redirect

from ..utils.cryptography import Cryptography
from ..utils.otp import OTPHandler
from ..repositories.customer import CustomerRepository


class LoginView(View):
    
    def get(self, request):
        return render(request, 'login.html')
        

    def post(self, request):
        error_message = None
        try:
            CustomerRepository.deleteUserSession(request)
            emailID = request.POST['email']
            password = request.POST['password']
            print(emailID, password)
            customerDetails = CustomerRepository.findByEmail(emailID)
            print(customerDetails)

            if customerDetails == None:
                error_message = 'Invalid email ID. Please enter valid Email ID'
                return render(request, 'login.html', {"error_message": error_message})

            print(customerDetails.email)

            # decrypt password
            decryptedPass = Cryptography.decryption(customerDetails.password)
            print("decryptedPass",decryptedPass, password)
            if password != decryptedPass:
                error_message = 'Invalid password. Please enter correct password.'
                return render(request, 'login.html', {"error_message": error_message})

            request.session['email'] = emailID
            request.session['customerId'] = customerDetails.id
            request.session['otpAction'] = 'login'
            
            otpObj = OTPHandler(request, emailID)
            otpObj.sentOTP()
            return redirect('otp')
        except Exception as e:
            print(e)
            return render(request, 'login.html', {"error_message": 'Something went wrong!!'})
