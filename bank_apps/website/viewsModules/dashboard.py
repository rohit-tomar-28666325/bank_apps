from django.views import View
from django.shortcuts import render, redirect

from ..utils.cryptography import Cryptography
from ..utils.otp import OTPHandler
from ..repositories.customer import CustomerRepository

from ..repositories.transaction import TransactionRepository


class DashboardView(View):

    def get(self, request):
        isSuccess = False
        tableData = []
        totalIncome = 0
        totalOutcome = 0
        totalBalance = 0
        error_message = ''

        try:
            customerId = request.session['customerId']
            if 'errorMessage' in request.session:
                error_message = request.session['errorMessage']
                request.session['errorMessage'] = ''
            
            tableData, totalIncome, totalOutcome, totalBalance = TransactionRepository.getTransactionList(
                customerId)

        except Exception as e:
            print(e)
            pass

        return render(request, 'main.html', {'username': request.session['customerName'], 'tableData': tableData, 'totalIncome': totalIncome,
                                             "totalOutcome": totalOutcome, "totalBalance": totalBalance, "isSuccess": isSuccess, "error_message": error_message})

    def post(self, request):
        customerId = request.session['customerId']
        amount = request.POST['amount']
        transType = request.POST['transType']
        errorMessage = ''
        customerId = request.session['customerId']
        status = False
        tableData, totalIncome, totalOutcome, currentBalance = TransactionRepository.getTransactionList(
            customerId)
        if transType == TransactionRepository.transactionType.get('depositType'):
            summary = request.POST['remark']
            status, errorMessage = TransactionRepository.deposit(
                customerId, amount, transType, summary)

        elif transType == TransactionRepository.transactionType.get('withdrawType'):
            summary = request.POST['remark']
            status, errorMessage = TransactionRepository.withdraw(
                customerId, amount, currentBalance, transType, summary)

        elif transType == TransactionRepository.transactionType.get('transferType'):
            otherAccountNo = request.POST['account_number']
            status, errorMessage = TransactionRepository.transfer(request, otherAccountNo, amount, currentBalance, transType)

        request.session['errorMessage'] = errorMessage
        return redirect('main')


def my_redirect_view(request):
    context_data = request.GET.get('key', None)
    # Your redirected view logic here
    return render(request, 'my_template.html', {'key': context_data})
