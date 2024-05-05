from django.views import View
from django.shortcuts import render, redirect

from ..utils.cryptography import Cryptography
from ..utils.otp import OTPHandler
from ..repositories.customer import CardsRepository

class CardView(View):
    
    def get(self, request):
        return render(request, 'card.html')
    
    def post(self, request):
        request.session['tempData0'] = request.POST
        if request.POST['actionBtn'] == 'Proceed':
            return redirect('dashboard')

