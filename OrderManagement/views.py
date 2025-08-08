from django.shortcuts import render,redirect

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required   

@login_required(login_url='/') 
def CustomerList(request):
    customers = Customer.objects.all()
    context = {
        'allcustomers': customers
    }
    return render(request, 'customers_view.html', context)

@login_required(login_url='/') 
def CustomerAdd(request):
    
    if request.user.role == 2:
        return render(request, 'unauthorized.html')
    context={
        'customer_form': Customer_Form()
    }    
    if request.method == 'POST':
        customer_form= Customer_Form(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/orders/customers/')
    return render(request, 'customersadd.html',context)

@login_required(login_url='/')  
def CustomerUpdate(request, id):
    if request.user.role == 2:
        return render(request, 'unauthorized.html')

    selected_customer = Customer.objects.get(id=id)
    
    context={
        "customer_form":Customer_Form(instance=selected_customer)
    }
    if request.method=="POST":
        customer_form=Customer_Form(request.POST,instance=selected_customer)
        if  customer_form.is_valid():
             customer_form.save()
        return redirect('/orders/customers/')
    return render(request, 'customersadd.html', context)

@login_required(login_url='/') 
def DeleteCustomer(request, id):
    if request.user.role == 2:
        return render(request, 'unauthorized.html')

    selected_customer = Customer.objects.get(id=id)
    selected_customer.delete()
    return redirect('/orders/customers/')

@login_required(login_url='/') 
def OrdersAdd(request):
    context={
        'order_form':Orders_Form()
    }
    if request.method == 'POST':
        customer_id = request.POST.get('Customer_reference')
        product_id = request.POST.get('product_reference')
        order_number = request.POST.get('order_number')
        order_date = request.POST.get('order_date')
        quantity = request.POST.get('quantity')

        if customer_id and product_id and quantity:
            quantity = int(quantity)
            selected_product = Product.objects.get(id=product_id)
            amount = float(selected_product.price) * quantity
            gst_amount = (amount * selected_product.gst) / 100
            bill_amount = amount + gst_amount

            new_order = Orders(
                Customer_reference_id=customer_id,
                product_reference_id=product_id,
                order_number=order_number,
                order_date=order_date,
                quantity=quantity,
                amount=amount,
                gst_amount=gst_amount,
                bill_amount=bill_amount
            )
            print("New Order Created:", new_order)
            new_order.save()
            return redirect('/orders/orders/')
    return render(request,'orders_add.html',context)


@login_required(login_url='/') 
def OrderList(request):
    context = {
        'all_orders':Orders.objects.all()
    }
    return render(request, 'orders.html', context)

@login_required(login_url='/') 
def OrderDelete(request,id):
    order=Orders.objects.get(id=id)
    order.delete()
    return redirect('/orders/orders/')

@login_required(login_url='/') 
def OrderUpdate(request, id):
    order=Orders.objects.get(id=id) 
    context = {
        'order_form': Orders_Form(instance=order)
    }  
    if request.method == 'POST':
        customer_id = request.POST.get('Customer_reference')
        product_id = request.POST.get('product_reference')
        order_number = request.POST.get('order_number')
        order_date = request.POST.get('order_date')
        quantity = request.POST.get('quantity')

        if customer_id and product_id and quantity:
            quantity = int(quantity)
            selected_product = Product.objects.get(id=product_id)
            amount = float(selected_product.price) * quantity
            gst_amount = (amount * selected_product.gst) / 100
            bill_amount = amount + gst_amount
            order_filter=Orders.objects.filter(id=id)
            order_filter.update(Customer_reference_id=customer_id,
                product_reference_id=product_id,
                order_number=order_number,
                order_date=order_date,
                quantity=quantity,
                amount=amount,
                gst_amount=gst_amount,
                bill_amount=bill_amount)
            
            return redirect('/orders/orders/')
    return render(request, 'orders_add.html', context)
