from email import message
from pyexpat.errors import messages
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import pic
#------------------------

def home(request):
    obj = pic.objects.all().order_by('-dat')
    context = {'obj': obj}
    return render(request, 'index.html', context)




def category(request):
    return render(request, 'category.html')

def single(request):
    return render(request, 'single.html')

def contact(request):
    return render(request, 'contact.html')

#--------------------------login and register with logout
def logout(request):
    auth.logout(request)
    messages.success(request,'logged out succesfully!!!!!!')
    return redirect('/')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']

        if pwd1==pwd2:
            if User.objects.filter(username=uname).exists():
                messages.warning(request,', Username Taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,', Email Taken!')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=uname,password=pwd1,email=email,first_name=fname,last_name=lname)
                user.save()
                auth.login(request,user)
                messages.success(request,',  Registered and logged in successfully!')
                return redirect('/')
        else:
            messages.error(request,'Password not matching!')
            return redirect('register')  
    else:
            return render(request,'registration/register.html')





