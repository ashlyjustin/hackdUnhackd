from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProf(models.Model):
	user_name = models.OneToOneField(User,on_delete=models.CASCADE)
	# def __str__(self) :
	# 	return self.User.user

class Job(models.Model):
	userName=models.ForeignKey(UserProf,on_delete=models.CASCADE)
	jobName=models.CharField(max_length=16)
	jobDesc=models.CharField(max_length=16)
	skillReq=models.CharField(max_length=16)
	salary = models.CharField(max_length=10)




	
 