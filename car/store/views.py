
from django.shortcuts import redirect, render
from django.contrib import messages
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import pymysql


# Create your views here.

def home(request):
    return render(request,"store/index.html")


def company(request):
    company = Company.objects.filter(nowheel=4)
    context ={'company':company}
    return render(request,"store/company.html",context)    

def companyview(request,slug):
    if(Company.objects.filter(slug=slug)):
         products= Product.objects.filter(slug=slug)
         company_name=Company.objects.filter(slug=slug)
         context={'products':products ,'company_name':company_name}
         return render(request,"store/products/index.html",context)
    else:
        messages.warning(request,"no such company found")
        return redirect('company')
def productview(request,comp_slug,prod_slug):
    if(Company.objects.filter(slug=comp_slug)):
        if(Product.objects.filter(slug=prod_slug)):
            products=Product.objects.filter(slug=prod_slug).first
            context={'products':products}
        else:
            messages.warning(request,"no such company found")
            return redirect('company')     
    else:
        messages.warning(request,"no such product found")
        return redirect('company')
    return render(request,"store/products/view.html",context)        

def searchcar(request):
    if request.method=="POST":
             type=(request.POST.get("cartype"))
             con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',passwd='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')
             curs=con.cursor()
             curs.execute("select * from store_product where cartype='%s'" %type)
             data=curs.fetchall()
             con.close()
             return render(request,"store/company.html",{"list":data})                         

def signup(request):
    if request.method== "POST":
        # username = request.POST.get('username')
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request,"your account has been succesfully created")

        return redirect("signin")
    return render (request,"store/signup.html")

def signin(request):
    if request.method== "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            fname= user.first_name
            return render(request,"store/index.html", {'fname':fname})
        else:
            messages.error("bad credentials")
        return redirect("home.html")
    return render (request,"store/signin.html")

def signout(request):
     pass