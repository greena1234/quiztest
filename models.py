from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Choice(models.Model):
	"""choice model"""
	
	choice_text1 = models.CharField(max_length=200,null=True,blank=True)
	choice_text2 = models.CharField(max_length=200,null=True,blank=True)
	choice_text3 = models.CharField(max_length=200,null=True,blank=True)

	
class Question(models.Model):
	"""question model"""
	question=models.CharField(max_length=200,null=True,blank=True)
	answer=models.ForeignKey(Choice, on_delete=models.CASCADE)

	def __str__(self):
		return self.question
