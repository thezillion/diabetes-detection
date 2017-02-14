

from django.db import models


class Person(models.Model):
	def __init__(self,name, age, insulin, gender, email, bmi,bp, glucose):
		self.name=name
		self.age=age
		self.gender=gender
		self.email=email
		self.bmi=bmi
		self.bp=bp
		self.glucose=glucose

	name=models.CharField(max_length=20)
	age=models.IntegerField(default=0)
	insulin=models.IntegerField(default=0)
	GENDER_CHOICES=(
		('M','Male'),
		('F','Female')
		)
	gender=models.CharField(max_length=1, choices= GENDER_CHOICES)

	email=models.CharField(max_length=20)
	bmi=models.IntegerField(default=0)
	bp=models.IntegerField(default=0)
	glucose=models.IntegerField(default=0)
	

# Create your models here.
