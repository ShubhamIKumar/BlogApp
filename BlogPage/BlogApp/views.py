from django.shortcuts import render, redirect,HttpResponse
from .forms import UserForm
from .models import Info
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

def Signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1!=pass2:
                messages.error(request,"Password Mismatch")
                return redirect('signup')
            myuser = User.objects.create_user(username,email,pass1)
            myuser.save()
            form.save() 
            return redirect('login')
    else:
        form = UserForm()
        return render(request,'Signup.html',{'form':form})



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f' welcome {username} !!')
            return render(request, 'User.html')
        else:
            messages.info(request,'account done not exist plz sign in')
            return render(request, 'Login.html')
    
    return render(request, 'Login.html')

def logout(request):
        logout(request)
        messages.success("Successfully Log Out")
        return redirect('login')
        



