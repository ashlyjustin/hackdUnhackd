from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user_name = models.OneToOneField(User,on_delete=models.CASCADE)
	user_pic = models.ImageField(upload_to='profile_pics')


	# def __str__(self) :
	# 	return self.User.user

class Skills(models.Model):
	userName=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
	skill1=models.CharField(max_length=16)
	skill2=models.CharField(max_length=16)
	skill3=models.CharField(max_length=16)
	extraSkills = models.CharField(max_length=264)




	
 