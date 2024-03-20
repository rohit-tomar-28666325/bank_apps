from django import forms  
from website.models import Customers  
class CustomersForm(forms.ModelForm):  
    class Meta:  
        model = Customers  
        widgets = {
        'password': forms.PasswordInput(),
    }
      
        fields = "__all__"  