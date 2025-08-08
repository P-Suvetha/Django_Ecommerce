from django.urls import path,include
from .views import *

urlpatterns=[
    path('products/', AllProducts),
    path('products/add/', ProductAddPage),
    
    path('products/delete/<int:id>/', DeleteProducts,name='product_delete'),
    path('products/update/<int:id>/', ProductUpdate,name='product_update'),

]
