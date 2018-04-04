from django.shortcuts import render
from . import forms
from user_login.forms import UserForm,UserProfileForm
from client_login.models import Job,UserProf
from user_login.models import UserProfile
from django.contrib.auth import views as auth_views

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,'index.html')
def homepage(request):
	return render(request,'index.html')

@login_required	
def user_page(request):
	allJobs = Job.objects.all()
	allProf = UserProfile.objects.all()
	context = {'allJobs':allJobs}
	return render(request,'user_login/user.html',context)

def apply_page(request):
	return render(request,'user_login/apply.html')
	
@login_required
def special(request):
	return HttpResponse("Logged Out")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data =request.POST)
		# profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() :
		# and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			# profile = profile_form.save(commit=False)
			# profile.user = user

			# if'user_pic' in request.FILES:
			# 	profile.user_pic=request.FILES['user_pic']

			# profile.save()

			registered=True
		else:
			print(user_form.errors)

	else:
	 		user_form=UserForm()
	 		

	return render(request,'user_login/register.html',
	 				{'user_form':user_form,
	 					'registered':registered})

def user_login(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('user_login:user_page'))

			else:
				return HttpResponse("ACCOUNT NOT is_active")
		else:
			print("Tried Login and Failed")
			print("Username:{} and password {}".format(username,password))
			return HttpResponse("Invalid Login Details")
	else:
		return render(request,'user_login/login.html',{})


	
