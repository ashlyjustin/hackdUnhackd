from django import forms
from client_login.models import UserProf
from client_login.models import Job
from django.contrib.auth.models import User

class ClientForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model=User
		fields = ('username','first_name','last_name','email','password')
		

class ClientProfileForm(forms.ModelForm):
	
	designation = forms.CharField(required=False)
	class Meta():
		model=UserProf
		fields = ('designation',)
			
class JobForm(forms.ModelForm):
	class Meta():
		model = Job
		fields = '__all__'
