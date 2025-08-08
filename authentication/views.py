from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import User


def LoginPage(request):

    if request.user.is_authenticated:
        if request.user.role == 0:
            return redirect('/orders/customers/')
        elif request.user.role == 1:
            return redirect('/inventory/products/')
        else:
            return redirect('/orders/orders/')


    context = {
           "error":""
    }
    if(request.method == "POST"):
        print(request.POST,flush=True)
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        print(user)
    
        if user is not None:
            login(request,user)
            if user.role == 0:
                return redirect('orders/customers')
            elif user.role == 1:
                return redirect('inventory/products')
            return redirect('orders/customers')  # Assuming you have a home view in your inventory app
        else:
            context={
                "error":"*Invalid username or password. Please try again."
            }
            
    return render(request, 'login.html',context)


def LogoutPage(request):
    logout(request)
    return redirect('login')
def SignUpPage(request):
    context = {
        "error": ""
    }

    if request.method == "POST":
        username = request.POST.get('username')
        user_check = User.objects.filter(username=username)

        if user_check.exists():
            context["error"] = "*Username already exists"
            return render(request, 'signup.html', context)

        # ✅ Cast role to int so it saves correctly
        new_user = User(
            username=username,
            first_name=request.POST.get('firstname'),
            last_name=request.POST.get('lastname'),
            email=request.POST.get('email'),
            age=request.POST.get('age'),
            role=int(request.POST.get('user_role')),  # ✅ FIXED
        )
        new_user.set_password(request.POST.get('password'))
        new_user.save()
        return redirect('login')

    return render(request, 'signup.html', context)
