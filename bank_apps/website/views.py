from django.shortcuts import render, HttpResponse, redirect
from website.forms import CustomersForm 
import pyotp
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail
from website.forms import CustomersForm, TransactionForm 
from website.models import Customers, Transaction
from django.db.models import Sum
import datetime


def home(request):
    return render(request, 'login.html', {'title': 'home'})

def about(request):
    return render(request, 'login.html', {'title': 'about'})

def login(request):
    error_message =None
    if request.method == 'POST':
        emailID = request.POST['email']
        password = request.POST['password']
        if Customers.objects.filter(email=request.POST['email']).exists():
            if Customers.objects.filter(email=request.POST['email'])[0].password == password:
                username = Customers.objects.filter(email=request.POST['email'])[0].last_name
                send_otp(request, emailID)
                request.session['username'] = username
                request.session['email'] = emailID
                return redirect('otp')
            else:
                error_message = 'Invalid password. Please enter correct password'
                pass
        else:
           error_message = 'Invalid email ID. Please enter valid Email ID'
           pass
    return render(request, 'login.html', {"error_message": error_message})
    
def main(request):
    isSuccess = False
    if request.method == "POST":  
        print('block entered123', request.session['email'])
        form = TransactionForm(request.POST)  
        if form.is_valid():  
            print('block entered')
            try: 
                print('try block entered')
                form.instance.email = request.session['email'] 
                form.instance.date = datetime.datetime.now().strftime("%d/%m/%Y")
                form.instance.status = "Success" 
                form.save()  
                isSuccess = True;
                return redirect('main')

            except:  
                   pass
    else:  
        form = TransactionForm()  

    tableData = Transaction.objects.all().order_by('-pk') 
    loggedInUserData = Transaction.objects.filter(email=request.session['email'])
    totalIncome = Transaction.objects.filter(transType="deposit").aggregate(total_amount=Sum('amount'))['total_amount']
    totalOutcome = Transaction.objects.exclude(transType="deposit").aggregate(total_amount=Sum('amount'))['total_amount']
    if(totalIncome == None):
        totalIncome = 0
    if(totalOutcome == None):
        totalOutcome = 0
    totalBalance = totalIncome - totalOutcome

    return render(request, 'main.html',{'username': request.session['username'], 'tableData' : tableData, 'totalIncome' : totalIncome,
    "totalOutcome" : totalOutcome, "totalBalance" : totalBalance, "isSuccess": isSuccess})

def signup1(request):
    if request.method =="POST" :
         request.session['tempData1'] = request.POST
         if request.POST['actionBtn'] == 'Proceed':
             return redirect('signup2')

    return render(request, 'signup1.html')

def signup2(request):
    if request.method =="POST" :
         request.session['tempData2'] = request.POST
         if request.POST['actionBtn'] == 'Proceed':
            return redirect('signup3')
         else:
            return redirect('signup1')
    return render(request, 'signup2.html')

def signup3(request):
    if request.method =="POST" :
         request.session['tempData3'] = request.POST
         if request.POST['actionBtn'] == 'Proceed':
             return redirect('signup4')
         else:
             return redirect('signup2')
    return render(request, 'signup3.html')

def signup4(request):
    if request.method == "POST":
        request.session['tempData4'] = request.POST
   
        if request.POST['actionBtn'] == 'Proceed':
             send_otp(request, dict(request.session['tempData2'].items()).get('email'))
             return redirect('otp')
        else:
             return redirect('signup3')

    return render(request, 'signup4.html')

def addNewUserDataToDatabase(request):
    if request.method == "POST": 
        form = CustomersForm(request.POST)  
        if form.is_valid(): 
            try:  
                form.instance.title = dict(request.session['tempData1'].items()).get('title')
                form.instance.first_name = dict(request.session['tempData1'].items()).get('first_name')
                form.instance.middle_name = dict(request.session['tempData1'].items()).get('middle_name')
                form.instance.last_name =dict(request.session['tempData1'].items()).get('last_name')
                form.instance.email = dict(request.session['tempData2'].items()).get('email')
                form.instance.phone_number= dict(request.session['tempData2'].items()).get('phone_number')
                form.instance.dob =dict(request.session['tempData2'].items()).get('dob')
                form.instance.address =dict(request.session['tempData3'].items()).get('address')
                form.instance.city=dict(request.session['tempData3'].items()).get('city')
                form.instance.country= dict(request.session['tempData3'].items()).get('country')
                form.instance.postal_code =dict(request.session['tempData3'].items()).get('postal_code')
                form.instance.password =dict(request.session['tempData4'].items()).get('password')
                form.instance.status = "Active"
                form.save() 
                return
            except Exception as e:  
                pass  
        else:
            pass

def formOTP(request):
    otp1 = request.POST['otp1'];
    otp2 = request.POST['otp2'];
    otp3 = request.POST['otp3'];
    otp4 = request.POST['otp4'];
    otp5 = request.POST['otp5'];
    otp6 = request.POST['otp6'];
    otp = otp1+otp2+otp3+otp4+otp5+otp6
    return otp

def otp(request):
    error_message =None
    if request.method == 'POST':
        otp = formOTP(request)
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_date']   
        if otp=="":
            error_message ="Please enter OTP"
        elif request.session['otp'] != otp :
            error_message = "Invalid OTP. Please enter valid OTP" 
        elif datetime.fromisoformat(otp_valid_until) < datetime.now():
            error_message = "Password Epired. Please Login/ Sign Up again "
        else:
            error_message = None
        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)
            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval = 60)
                if totp.verify(otp):
                    if request.session['otp'] == formOTP(request) :
                        if request.POST['actionBtn'] == 'Verify Email':
                            addNewUserDataToDatabase(request)
                            request.session['username'] = dict(request.session['tempData1'].items()).get('last_name')  
                            return redirect('main')                         
                        else:
                            return redirect('signup1')
                    else :
                        if request.POST['actionBtn'] == 'Cancel':
                            return redirect('signup1')
                        else:
                            pass    
            else:   
                if request.POST['actionBtn'] == 'Cancel':
                    return redirect('signup1')
                else:
                    pass  
        else:
            if request.POST['actionBtn'] == 'Cancel':
                    return redirect('signup1')
            else:
                 pass  
    else:  
        pass      
    return render(request, 'otp.html',{"error_message" : error_message, "emailID": dict(request.session['tempData2'].items()).get('email')})
    
def send_otp(request, emailID):
    totp = pyotp.TOTP(pyotp.random_base32(), interval = 60)
    otp = totp.now()
    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now()+ timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)
    request.session['otp'] = otp
    #email functionality
    # subject = 'OTP Testing Mail'
    # message = f'Hi this is your OTP {otp}.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [emailID]
    # send_mail( subject, message, email_from, recipient_list )

    print(f"YOUR OTP IS {otp}")
