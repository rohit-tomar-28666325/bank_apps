from django.contrib import admin
# Register your models here.


from .models.models import Customers, Transaction, Cards
admin.site.register(Customers)
admin.site.register(Transaction)
admin.site.register(Cards)
