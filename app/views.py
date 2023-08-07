from django.http import HttpResponse,Http404

# Create your views here.
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import View
from app.forms import signupForm,room_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from app.models import CustomUser,room_model
# ============================================================


@login_required
def profile(request):
        
    if request.method == 'POST':
        rm=room_form(request.POST)

        if rm.is_valid():
            room= rm.cleaned_data['room']
            reg = room_model(room=room,slug=room)
            reg.save()
        # stor = request.POST.get('room')          # here i get room name from: name = 'room'

        stor = room_model.objects.get(room = room)
        print('inside the store value..',stor)
        room_id = stor
        return redirect(f'/room/{room_id}/')
    else:
        rm= room_form()
        created_rooms = room_model.objects.all()
        return render(request,'app/profile.html',{'room':rm,'created_rooms':created_rooms})
    #  check mypro 30 for error concept


def home(request) -> HttpResponse:
    return render(request,'app/home.html')


# @login_required()            
def user_chat(request,group):
    roomname=group
    print('room name--->',roomname)    
    print('type of  room name--->',type(roomname))    
    return render(request,'app/chatpage.html',{'groupname':group})    

def get_room_func(request,slug):
    get_room= room_model.objects.get(slug=slug)
    print('inside the get_room --->',get_room)
    return redirect(f'/room/{get_room}/')


class signupView(View):
    def get(self, request, *args, **kwargs):
        fm = signupForm()
        return render(request,'app/signup.html',{'form':fm})

    def post(self, request, *args, **kwargs):
        fm= signupForm(request.POST)
        if fm.is_valid():
            us= fm.cleaned_data['username']
            em = fm.cleaned_data['email']
            reg = CustomUser(username=us,email=em)
            reg.save()

        fm = signupForm()
        messages.success(request,'YOU SIGNEDUP SUCCESSFULLY !!!')    
        return HttpResponseRedirect('/')

def login_form(request):
    if request.user.is_authenticated:   
            
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)                        
                    # here the message is work when w logged out why!, bcos we redirect this page in {profile.html},jaha par message hamee define nahi kiya hai
                    messages.info(request,'you login successfully!!!')  
                    return HttpResponseRedirect('/profile/')
                else:
                    print('invalid credientials..')
    else:
        # this is for get request
        fm=AuthenticationForm()
    return render(request,'registration/login.html',{'form':fm})                
         
def logout_form(request):
    logout(request)
    messages.info(request,'you logged out successfully!!!')        
    # return redirect('/')
    return render (request,'registration/logout.html')


# ---------------------------------------------------------------------------------------------------------------------------

