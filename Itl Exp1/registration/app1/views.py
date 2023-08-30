from django.shortcuts import render,HttpResponse,redirect #HttpResponse,redirect should be imported manually
from django.contrib.auth.models import User #imported model
from django.contrib.auth import authenticate, login,logout #authenticate, login should be imported manually so that the username in the database and the username entered by the new customer should not be same; logout should be imported manually
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Employees,PartyDetails
from app1.models import Employees,PartyDetails
# Create your views here.
@login_required(login_url = 'login')#by this not everyone can access the home page just by typing the url of the home page
def INDEX(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return render(request, 'home1.html',context)

def ADD(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employees(name=name, email=email, address=address,phone=phone)
        emp.save()
        return redirect('home1')
    return render(request,'home1.html')

def EDIT(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return render(request, 'home1.html',context)

def UPDATE(request,id):
    if request.method == 'POST':
        # id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employees(id=id, name=name, email=email, address=address,phone=phone)
        emp.save()
        return redirect('home1')
    return render(request,'home1.html')

def DELETE(request,id):
    emp = Employees.objects.filter(id=id)
    emp.delete()
    context = {
        'emp':emp,
    }
    # emp.delete()
    return redirect('home1')

def HOMEPAGE(request):
 return render (request , 'homepage.html')
# def HomePage(request):
#  return render (request , 'home1.html')
def SignUpPage(request):
    if request.method=='POST':
      uname = request.POST.get('username')
      email = request.POST.get('email')
      pass1= request.POST.get('password1')
      pass2 = request.POST.get('password2')
      #to make sure both the passwords are same
      if pass1!=pass2:
        return HttpResponse("Your password and confirm password are not similar")
      else:
           my_user= User.objects.create_user(uname,email,pass1) #every entry will be stored in this variable
           my_user.save() #details are saved
           return redirect('login') #name = 'login' from urls.py and redirect('login') should be same
      
    return render (request , 'signup.html')
def LoginPage(request):
  if request.method=='POST':
      username = request.POST.get('username')
      pass1=request.POST.get('pass')
      #so that the username in the database and the username entered by the new customer should not be same
      user = authenticate(request, username = username, password = pass1)
      if user is not None:
         login(request, user)
         return redirect('homepage')
      else:
         return HttpResponse("Username or Password is incorrect!!")
  return render(request , 'login.html')

# def LogoutPage(request):
#   logout(request)
#   return redirect('login')

# def GalleryPage(request):
#    return render(request, 'gallery.html')
# def FAQPage(request):
#    return render(request, 'faq.html')
# def VenuePage(request):
#    return render(request, 'venue.html')
def FormPage(request):
     if request.method=='POST':
      firstname = request.POST.get('firstname')
      email = request.POST.get('email')
      lastname = request.POST.get('lastname')
      date= request.POST.get('date')
      date1= request.POST.get('date1')
      guest= request.POST.get('guest')
      party= request.POST.get('party')
      budget = request.POST.get('budget')
      theme = request.POST.get('theme')
      info = request.POST.get('info')
     # Here you can process the form data as per your requirements
        # For example, you can store it in the database or perform any other operations
         # Create a new instance of PartyDetails model
         #i.e make a new db on the admin page
      party_details = PartyDetails(
            first_name=firstname,
            # last_name=lastname,
            # email=email,
            # party_date=date,
            # suppliers_date=date1,
            guest_count=guest,
            # party_type=party,
            budget=budget,
            # theme=theme,
            # additional_info=info
        ) #every entry will be stored in this variable
      # Save the PartyDetails instance to the database
      party_details.save()
        # Return a success message
    #   return HttpResponse("Form submitted successfully!")
      return redirect('home1')
      

    # If the request method is GET or any other method, render the form page
     return render(request, 'form.html')

