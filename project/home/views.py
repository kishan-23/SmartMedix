
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from user import views as vw
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request, 'home/entrypage.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def doctor(request):
    return render(request, 'home/doctor.html')


def handleSignUp(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        chk = request.POST.getlist('checks')
        #print(flexCheckDefaultdoctor)

        print(username)

        # here i am applying checklist
        if (len(username) > 10):
            messages.error(
                request, 'Username must contain less than 10 characters')
            return redirect('home')

        if (pass1 != pass2):
            messages.error(request, 'password does not match')
            return redirect('home')

        if (not username.isalnum()):
            messages.error(
                request, 'Username must contain alphanumeric characters')
            return redirect('home')

        # creating the user in django
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, 'Your SmartMedix account has been created successfully')

        if 1 in chk:
            myuser.groups.add(1)
        
        if 2 in chk:
            myuser.groups.add(2)

        
        return redirect('user-index',names=username)

    else:
        return HttpResponse('404 Not Found')


def handlelogin(request):
    if (request.method == 'POST'):
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        # here i am taking user that is authenticated
        user = authenticate(username=loginusername, password=loginpassword)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "SuccessFully Logged in")
            return redirect('user-index',names=loginusername)
            if 'Doctor' in user.groups:
                print('Doctor')
                return HttpResponseRedirect(reverse('user-index', names='hello'))
            else:
                st = '/user/'+loginusername
                print('User')
                return redirect('user-index',names=loginusername)
        else:
            messages.error(request, "Invalid username and password")
            return redirect()

    return HttpResponse('404 not found')


def handlelogout(request):
    logout(request)
    messages.success(request, "SuccessFully logout")
    return redirect('home')
