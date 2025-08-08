from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required   

@login_required(login_url='/') 

def FullView(request):
    # Single role
    role = 'teacher'
    users = [
        {
            "name": "Suvetha",
            "email": "suvetha309@gmail.com",
            "role": "student",
            "number": [1, 3, 5, 7, 9],
            "marks": {
                "tamil": 50,
                "english": 45,
                "maths": 47
            }
        },
        {
            "name": "Arun",
            "email": "arun456@gmail.com",
            "role": "teacher",
            "number": [2, 4, 6],
            "marks": {
                "tamil": 60,
                "english": 55,
                "maths": 65
            }
        },
        {
            "name": "Deepa",
            "email": "deepa789@gmail.com",
            "role": "admin",
            "number": [9, 7],
            "marks": {
                "tamil": 70,
                "english": 75,
                "maths": 80
            }
        }
    ]


    # Personal data
    content = {
        "name": "Suvetha",
        "email": "suvetha309@gmail.com",
        "number": [1, 3, 5, 7, 9],
        "marks": {
            "tamil": 50,
            "english": 45,
            "maths": 47
        }
    }

    # Combine everything into one context
    context = {
        'role': role,
        'users': users,
        'name': content["name"],
        'email': content["email"],
        'number': content["number"],
        'marks': content["marks"]
    }

    return render(request, 'home.html', context)

    return render(request, 'services.html')
@login_required(login_url='/')
def ProductAddPage(request):
    # ❌ Employees cannot add producs
    if request.user.role == 2:
        return render(request, 'unauthorized.html')  # Optional custom page

    context = {
        'product_form': Product_Form(),
    }

    if request.method == 'POST':
        product_form = Product_Form(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')
    return render(request, 'productsadd.html', context)

@login_required(login_url='/') 
def AllProducts(request):

    context = {
        'allproducts': Product.objects.all()
    }
    return render(request, 'products_view.html', context)

@login_required(login_url='/')
def DeleteProducts(request, id):
    if request.user.role == 2:
        return render(request, 'unauthorized.html')
    Product.objects.get(id=id).delete()
    return redirect('/inventory/products/')


@login_required(login_url='/')
def ProductUpdate(request, id):
    if request.user.role == 2:
        return render(request, 'unauthorized.html')

    product = Product.objects.get(id=id)
    context = {
        "product_form": Product_Form(instance=product)
    }
    if request.method == "POST":
        product_form = Product_Form(request.POST, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')
    return render(request, 'productsadd.html', context)
