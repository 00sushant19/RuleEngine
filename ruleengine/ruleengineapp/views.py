from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method=='POST':
        email=list(request.POST.getlist('email'))[0]
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        print(email,password,confirm_password,list(request.POST.getlist('email')))
        if password!=confirm_password:
            return HttpResponse("password incorrect")
        
        try:
            if User.objects.get(username=email):
               return HttpResponse("email exists")
        except Exception as identifier:
            pass
        user = User.objects.create_user(username = email,email=email,password=password)
        user.save()
        return HttpResponse("User created",email)
    return render(request,"signup.html")


def handlelogin(request):
    if request.method=='POST':
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser = authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return render(request,'index.html')
        else:
            messages.error(request,"invalid Credentials")
            return redirect(request,'login.html')
    return render(request,'login.html')
def handlelogout(request):
    return redirect('/login')