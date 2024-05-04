from django import forms  
from .models.models import Customers  
from .models.models import Transaction  
class CustomersForm(forms.ModelForm):  
    class Meta:  
        model = Customers  
        widgets = {
        'password': forms.PasswordInput(),
    }
        fields = "__all__"  


class TransactionForm(forms.ModelForm):  
    class Meta:  
        model = Transaction     
        fields = "__all__"  