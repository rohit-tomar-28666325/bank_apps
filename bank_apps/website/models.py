from django.db import models  
class Customers(models.Model):   
    title = models.CharField(max_length=10, blank=True, default='')
    first_name = models.CharField(max_length=100, blank=True, default='')  
    middle_name = models.CharField(max_length=100, blank=True, default='') 
    last_name = models.CharField(max_length=100, blank=True, default='') 
    email = models.CharField(max_length=100, blank=True, default='') 
    phone_number= models.CharField(max_length=10, blank=True, default='')
    dob =models.CharField(max_length=15, blank=True, default='') 
    address = models.CharField(max_length=150, blank=True, default='')
    city= models.CharField(max_length=150, blank=True, default='')
    country=  models.CharField(max_length=15, blank=True, default='')
    postal_code = models.CharField(max_length=15, blank=True, default='')
    password = models.CharField(max_length=15, blank=True, default='')
    status = models.CharField(max_length=15, blank=True, default='')
    confirm_password = models.CharField(max_length=15,blank=True, default='')
    actionBtn = models.CharField(max_length=15, blank=True, default='')
    class Meta:  
        db_table = "customers"  
