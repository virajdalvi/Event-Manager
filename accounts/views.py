from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, request

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            if (any(i.isdigit() for i in first_name)) == True:
                messages.info(
                    request, 'First Name cannot contain number or special characters')
                return redirect('cregister')
            if (any(j.isdigit() for j in last_name)) == True:
                messages.info(
                    request, 'Last Name cannot contain number or special characters')
                return redirect('cregister')
            if (first_name.isalpha()) == False:
                messages.info(
                    request, 'First Name cannot contain number or special characters')
                return redirect('register')
            if (last_name.isalpha()) == False:
                messages.info(
                    request, 'Last Name cannot contain number or special characters')
                return redirect('register')
            if User.objects.filter(username='').exists():
                messages.info(request, 'Username is empty')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()

                return redirect('login')
        else:
            messages.info(request, 'password not matching...')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def clogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('cdashboard')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('clogin')
    else:
        return render(request, 'clogin.html')


def cregister(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('cregister')
            if (any(i.isdigit() for i in first_name)) == True:
                messages.info(
                    request, 'First Name cannot contain number or special characters')
                return redirect('cregister')
            if (any(j.isdigit() for j in last_name)) == True:
                messages.info(
                    request, 'Last Name cannot contain number or special characters')
                return redirect('cregister')
            if User.objects.filter(username='').exists():
                messages.info(request, 'Username is empty')
                return redirect('cregister')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('cregister')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()

                return redirect('clogin')
        else:
            messages.info(request, 'password not matching...')
            return redirect('cregister')
        return redirect('/')

    else:
        return render(request, 'cregister.html')


def clogout(request):
    auth.logout(request)
    return redirect('/')
