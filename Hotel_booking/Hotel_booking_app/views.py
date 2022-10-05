from audioop import reverse
import email
import http
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView
from django.views import View, generic
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.

def Home(request):
    if not request.user.is_authenticated:
        return render(request,'home.html')
    
    else:
        return redirect('/userhome/')

def Sign_up(request):
    if request.method=='POST':
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm=SignUpForm()

    return render(request,'signup.html',{'form':fm})


def Log_in(request):
    if request.method=='POST':
        fm=LoginForm(request.POST)
        if fm.is_valid():
            
          
            
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            user=authenticate(password=password,email=email)

            if user is not None:
                login(request,user)
                # return HttpResponse('loged in')
                # st=CustomeUser.objects.all()
                # messages.success(request,'you are loged in!!{{user.first_name}}')
                return HttpResponseRedirect('/userhome/')
        else:
            er='Email/password is required'
            return render(request,'login.html',{'error':er})
    else:
        fm=LoginForm()
    return render(request,'login.html',{'form':fm})


def log_out(request):
    if request.method=="GET":
        logout(request)
        return redirect('/')


def Profile(request,id):
    # if request.user.is_authenticated:
       
    #     user=CustomeUser.objects.filter(id=request.user.id).first()
    #     # user=get_user_model.objects.all()
        
    #     fm=ProfileForm(instance=user)
       
    #     return render(request,'profile.html',{'users':fm})
    # else:
    #     return HttpResponseRedirect('/login/')

    if request.user.is_authenticated:
        user=CustomeUser.objects.get(pk=id)
        
        return render(request,'profile.html',{'users':user})

    else:
         return HttpResponseRedirect('/')
    # if request.method=="GET":
    #     user = CustomeUser.objects.get(pk=id)
    #     return render(request, 'profile.html',{'user':user})


def userhome(request):

    a=CustomeUser.objects.get(id=request.user
    .id)
    
    # import pdb;pdb.set_trace()
    return render(request,'userhome.html',{'qr':a})

    

# @csrf_exempt
# def Update_profile(request):
    
#         if request.method=='POST':
#             fm=ProfileForm(request.FILES,request.POST
#             )
#             # import pdb;pdb.set_trace()  
#             if fm.is_valid():
#                 fm.save()
#                 return HttpResponseRedirect('/userhome/')

        
#         else:
#             if request.user.is_authenticated:
#                fm=ProfileForm(instance=request.user)
#             else:
#                 return HttpResponseRedirect('/')
#         return render(request,'update_profile.html',{'form':fm})
    


def Forgetpassword(request):
        if request.method=='POST':
            fm=SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()

                return http('password change successfully')
        
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request,'forgetpassword.html',{'form':fm})
    
# def Update_profile1(request):
#     if request.method=="POST":
#         fm=ProfileForm(request.FILES,instance=request.user)
#         if fm.is_valid():
#             fm.save()
#             return HttpResponseRedirect('/userhome/')

#     else:
#         fm=ProfileForm(instance=request.user)

#     return render(request,'update_profile1.html',{'form':fm})

class ProfileUpdate(generic.View):
    def get(self, request,id, *args, **kwargs,):
        if request.user.is_authenticated:
            pi=CustomeUser.objects.get(pk=id)
            form = UserForm(instance=pi)
            return render(request,'update_profile.html',{'form':form})
        else:
            return redirect('/')

    def post(self, request,id, *args, **kwargs,):
        # user_details = CustomeUser.objects.get(id=request.user.id)
        pi=CustomeUser.objects.get(pk=id)
        form = UserForm(request.POST, request.FILES, instance=pi)
        if form.is_valid():
            
            form.save()
            return redirect('/userhome/')
        else:
            print("no")
        return render(request,'update_profile.html',{'form':form})


class search_view(ListView):
    model=Hotel
    template_name='search.html'

    def get_queryset(self) :

        result=super().get_queryset()
        query=self.request.GET.get('search')
        if Hotel.objects.filter(city=query):

            result=Hotel.objects.filter(city=query)
        else:
             result=Hotel.objects.filter(name=query)
        
        
        return result


# class Room_view(generic.View):
#     model=Room
#     template_name='room.html'

#     def get_queryset(self):
        
#             rm=Room.objects.all()
#             query=self.request.GET.get('hotel')
#             rm=rm.filter(hotel__name=query)
            
#             return rm
        

def Room_view(request,hotel):

    if request.method=='GET':
        rm=Room.objects.filter(hotel__name=hotel)

        return render(request,'room.html',{'object_list':rm})
    



class Booking_view(generic.View):

    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            fm=BookingForm()
            return render(request,'booking.html',{'form':fm})
        else:
            return redirect('/')

    def post(self,request,*args, **kwargs):
        fm=BookingForm()
        if fm.is_valid():
            fm.save()
            return redirect('/userhome/')
        else:
            print('no')
        return render(request,'booking.html',{'form':fm})
