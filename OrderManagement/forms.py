from django.forms import ModelForm

from .models import *

class Customer_Form(ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        
class Orders_Form(ModelForm):
    class Meta:
        model=Orders
        fields=['Customer_reference','product_reference','order_number','order_date','quantity']
