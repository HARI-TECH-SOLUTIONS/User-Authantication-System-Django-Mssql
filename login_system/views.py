from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.http import HttpResponse
from logzero import logger
from .models import *
from django.contrib import auth 
from django.contrib.auth.models import User, auth
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['rpassword']

        logger.info('uname: {}, fname: {}, lname: {}, email: {}, password1: {}, password2: {}'.format(uname, fname, lname, email, password1, password2))

        if password1==password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'User Name Allready Exists....')
                return render(request,'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Allready Exists.....')
                return render(request,'signup.html')
            else:
                result = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=email, password=password1)
                result.save()
                messages.info(request,'User Created...')
                return render(request,'signup.html')
        else:
            messages.info(request,'Passwords not Matched')
            return render(request,'signup.html')

    else:
        return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']

        logger.info('email: {}, password: {}'.format(username, password))

        user = auth.authenticate(username=username, password=password)

        if user is None:
            user2 = auth.authenticate(username=User.objects.get(email=username), password=password)        

            logger.info('user: {}, user2: {}'.format(user,user2))

            if user2 is None:
                messages.info(request,'Invalid Login Details....')
                return render(request,'login.html')
                        
        if user is not None:
            auth.login(request,user)
            # messages.info(request,'Login Successfull....')
            return redirect('/u/home/')
            # return render(request,'home.html')
        elif user2 is not None:
            auth.login(request,user2)
            # messages.info(request,'Login Successfull....')
            return redirect('/u/home/')
            # return render(request,'home.html')
        else:
            messages.info(request,'Invalid Login Details....')
            return render(request,'login.html')

    else :
        return render(request,'login.html')


def home(request):
    if request.method == 'GET':
        user_details = User.objects.all()
        logger.info('user_details: {}'.format(user_details))
        return render(request,'home.html',{'user_details':user_details})
    else:
        return render(request,'home.html')


def logout(request):
    auth.logout(request)
    return redirect('/u/login/')
