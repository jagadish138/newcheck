from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import Reg_form,signup_form,log_In,forgot_pass
from .models import login_Register
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
       
        s_form = signup_form(request.POST)
       

        if s_form.is_valid():
            s_form.save()
            messages.success(request,"Your registered Successfully")


        #     name= s_form.cleaned_data['username']
            
        #     # email= s_form.cleaned_data['email']
        #     password= s_form.cleaned_data['password']

        #     addNew = User.objects.create(username=name,password=password)
        #     addNew.save()
    messages.error(request,"Plz enter all details")
           
    s_form=signup_form()
    context = {'s_form':s_form}
    return render(request,'signup.html',context)
  

def log_me(request):
    if request.method=='POST':
        s_form = log_In(request.POST)
        if s_form.is_valid():
            username = s_form.cleaned_data['username']
            password = s_form.cleaned_data['password']

            user =authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                
                return redirect('personal')
                
            
    s_form = log_In()
    context = {'s_form':s_form}
    return render(request,'signin.html',context)


    
def register(request):
    if request.method=='POST':
        s_form = Reg_form(request.POST)
        if s_form.is_valid():
            father = s_form.cleaned_data['father']
            mother= s_form.cleaned_data['mother']
            ag = s_form.cleaned_data['age']
            mob =s_form.cleaned_data['mobile']
            add = s_form.cleaned_data['address']

            p = login_Register(father=father,mother=mother,age=ag,mobile=mob,address=add)
            p.save()
            messages.success(request,'Registration successfull')
            information = login_Register.objects.all()
            context={"information": information}
            return render(request,'register_main_page.html',context)
           
        else:
            messages.error(request,'Details are not valid')
    else:
        s_form = Reg_form()
   
    context={"s_form":s_form}
    return render(request,'register.html',context)



def forgot_password(request):
    form = forgot_pass()
    if request.method == "POST":
        form = forgot_pass(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            old_password = form.cleaned_data['old_password']
            user = authenticate(username=username,password = old_password)
            if user is not None:
                u = User.objects.get(username=username)
                u.set_password(form.cleaned_data['password'])
                u.save()
            
    context ={'form':form}
    
    return render(request,'forgot_pass.html',context)


def personal(request):
   
    return render(request,'personal.html',{"hello":"hi"})

