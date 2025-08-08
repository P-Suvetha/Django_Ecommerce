from django.urls import path
from .views import *

urlpatterns=[
     path('customers/add/', CustomerAdd),
     path('customers/', CustomerList),
     path('customers/delete/<int:id>/', DeleteCustomer,name='customer_delete'),
    path('customerss/update/<int:id>/', CustomerUpdate,name='customer_update'),
    path('add/order/', OrdersAdd, name='orders_add'),  
    path('orders/', OrderList, name='orders_list'),
    path('delete/order<int:id>/', OrderDelete, name='order_delete'),
     path('update/order<int:id>/', OrderUpdate, name='order_update'),
    

]