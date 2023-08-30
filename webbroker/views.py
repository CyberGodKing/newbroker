from django.shortcuts import render
# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import ContactForm,RegisterUserForm,PasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
# Create your views here.
import datetime,time
from .models import Contact

def home(request):
    return render(request,"base.html",{})

def faq(request):
    return render(request,"sections/faq.html",{})

def terms(request):
    return render(request,"sections/terms.html")

def academy(request):
    return render(request,"sections/academy.html")
def passwordreset(request):
    return render(request,"passwordreset.html")
def loginuser(request):
    if request.method=="POST":
        user_email=request.POST['email']
        password=request.POST['password']
        try:
            usernames = User.objects.get(email=user_email)
            user=authenticate(request,username=usernames.username,password=password)
            if user is not None :
                login(request,user)
                return redirect('dashboard')
            else:
                #.success(request,('There was an error logging in, check credential and TRY AGAIN...'))
                return redirect('login')
        except User.DoesNotExist:
            pass
    else:
        return render(request,'login.html',{})

def signup(request):
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        contactform =  ContactForm(request.POST)
        if form.is_valid() and contactform.is_valid():
            form.save()
            edith=  contactform.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            edith.user = request.user
            edith.save()
            messages.success(request,('Account created successfully...'))
            return redirect('dashboard')
        else:
            messages.success(request,"An Error Occured..... ")
    else:        
        form = RegisterUserForm() 
        contactform = ContactForm()      
    return render(request,'signup.html',{'form':form,"form2":contactform})

def log_out(request):
    logout(request)
    return redirect('login')

def reset(request):
    user = request.user
    #edit   = user_detail.objects.get()
    if request.user.is_authenticated == False:
        messages.success(request,'You need logging access before you can access page...')
        return redirect("login")
    else:
        if request.method=="POST":
            form = PasswordForm(user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Password changed successfully..")
                return redirect('login')
            else:
                messages.success(request,"Error updating password .TRY AGAIN..")
                return redirect("reset")
        form = PasswordForm(user)
        text="Change Password"
        return render(request,'reset.html',{"form":form,"text":text})

def dashboard(request):
    if request.user.is_authenticated:
        text="Dashboard"
        return render(request,"dashboard.html",{"text":text})
    else:
        return redirect("login")

def profile(request):
    if request.user.is_authenticated == True:
        obj= Contact.objects.get(user=request.user)
        form= ContactForm(request.POST or None, instance=obj)
        if form.is_valid()==True:
            form.save()
            messages.success(request,"Profile Updated Successfully...")
            return redirect("profile")
        text="User Profile"
        return render(request,"profile.html",{"form":form,"text":text})
    else:
        return redirect("login")

def plan(request):
    if request.user.is_authenticated == True:
        text="Investment Plan"
        return render(request,"plan.html",{"text":text})
    else:
        return redirect("login")

def deposit(request):
    if request.user.is_authenticated == True:
        text="Deposit"
        return render(request,"deposit.html",{"text":text})
    else:
        return redirect("login")

def investment(request):
    if request.user.is_authenticated == True:
        text="My Investment"
        return render(request,"investment.html",{"text":text})
    else:
        return redirect("login")

def withdraw(request):
    if request.user.is_authenticated == True:
        text="Withdrawal"
        return render(request,"withdraw.html",{"text":text})
    else:
        return redirect("login")
    
def history(request):
    if request.user.is_authenticated == True:
        text="History"
        return render(request,"history.html",{"text":text})
    else:
        return redirect("login")
    
def downline(request):
    if request.user.is_authenticated == True:
        text="Downline"
        return render(request,"downline.html",{"text":text})
    else:
        return redirect("login")
def eth(request):
    if request.user.is_authenticated == True:
        #text="Downline"
        return render(request,"eth.html",{})
    else:
        return redirect("login")
def bitcoin(request):
    if request.user.is_authenticated == True:
        #text="Downline"
        return render(request,"btc_cash.html",{})
    else:
        return redirect("login")


