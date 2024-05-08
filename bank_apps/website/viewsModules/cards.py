from django.views import View
from django.shortcuts import render, redirect

import time
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from ..utils.cryptography import Cryptography
from ..utils.otp import OTPHandler
from ..repositories.customer import CardsRepository

class CardView(View):
    
    def get(self, request):
        customerId = request.session['customerId']
        cardDetails = CardsRepository.getCardDetails(customerId)

        print(cardDetails)

        if cardDetails == None:
            return redirect('login')

        context = {
            "cardmessage": "",
            "securitymessage": "",
            "pinmessage": "",
            "card_number": cardDetails['card_number'],
            "security_code": cardDetails['security_code'],
            "pin_number": cardDetails['pin_number']
        }

        print(context)
        return render(request, 'card.html', context=context)
    
    def post(self, request):
        pinmessage = ""
        try:
            customerId = request.session['customerId']
            cardDetails = CardsRepository.getCardDetails(customerId)
            if cardDetails == None:
                return redirect('login')

            context = {
                "cardmessage": "",
                "securitymessage": "",
                "pinmessage": "",
                "pin_number": cardDetails['pin_number']
            }

            if request.POST['actionBtn'] == 'Change Pin':
                data = {
                    'pin_number': request.POST['pin_number']
                }
                status = CardsRepository.updatePinNumb(request, data)
                if status:
                    context['pinmessage'] = "Update security Successfully"
                else:
                    context['pinmessage'] = "Something went wrong!"

        except Exception as e:
            print(e)
            return render(request, 'card.html', {"pinmessage": pinmessage})

