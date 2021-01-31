from django.shortcuts import render

# Create your views here.

# This is written for PYTHON 3
# Don't forget to install requests package

from django.shortcuts import render, redirect
import requests
import json
# register
from .models import BookUpload
from .forms import AccountForm, CustomerForm, BookForm, BookDisplay
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    #https://www.youtube.com/watch?v=Xj0MXHrAi9o
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # returns the user to us
            user = form.save()
            # log the user in
            # redirect user to another location
            # return redirect('articles:list')
            login(request, user)


    else:
        form = UserCreationForm()
    return render(request, "payments/signup.html", {'form':form})

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request,user)
            return redirect('')
    else:
        form = AuthenticationForm()
    return render(request,"payments/login.html",{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/payments/login')

def profile_view(request):
    msg = "You have successfully logged In"
    if request.user.is_authenticated:
        username = request.user.username
    context = {
        'msg': msg,
        'username': username
    }
    return render(request, "payments/profile.html", context)

def create_image(request):
    if request.method =='POST':
        form = BookForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            # log in the user
            form.save()
            obj=form.instance
    else:
        form = BookForm()

    context = {
        'form':form
    }
    return render(request,"payments/book_create.html",context)

def book_detail(request):
    c = {}
    c['goods'] = BookUpload.objects.all()
    return render(request, 'payments/book_detail.html', c)

def find_book(request):
    form = BookDisplay(request.POST or None)
    if request.method =='POST' and form.is_valid():
       form.save()
    else:
        form = BookDisplay()
    return render(request,"payments/userbooks.html",{'form':form})

