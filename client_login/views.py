from django.shortcuts import render
from . import forms
from client_login.forms import ClientForm, ClientProfileForm
from django.contrib.auth import views as auth_views

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from user_login.models import Skills,UserProfile
from django.http import JsonResponse
# Create your views here.
def index(request):
	return render(request,'index.html')
def homepage(request):
	return render(request,'index.html')

@login_required	
def user_page(request):
	
	return render(request,'client_login/client.html')


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
		user_form = ClientForm(data =request.POST)
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
	 		user_form=ClientForm()
	 		

	return render(request,'client_login/register.html',
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
				return HttpResponseRedirect(reverse('client_login:user_page'))

			else:
				return HttpResponse("ACCOUNT NOT is_active")
		else:
			print("Tried Login and Failed")
			print("Username:{} and password {}".format(username,password))
			return HttpResponse("Invalid Login Details")
	else:
		return render(request,'client_login/login.html',{})


def ItemApi(request):
	
	UserSkill = Skills.objects.all()
	
	skillsList = []

	for obj in UserSkill:
		tempData={
		"id" : obj.userName,
		"skill1": obj.skill1,
		"skill2":obj.skill2,
		"skill3":obj.skill3,
		"extra":obj.extraSkills
		}
		skillsList.append(tempData)

	data = {}
	data['success']=True
	data['item'] = skillsList

	return JsonResponse(data,safe=False)	

