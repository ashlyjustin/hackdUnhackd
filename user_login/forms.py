from django import forms
from user_login.models import UserProfile
from user_login.models import Skills
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields = ('username','first_name','last_name','email','password')
		

class UserProfileForm(forms.ModelForm):
	
	userpic = forms.ImageField(required=False)
	class Meta():
		model=UserProfile
		fields = ('user_pic',)
			
class SkillForm(forms.ModelForm):
	class Meta():
		model = Skills
		fields = '__all__'
