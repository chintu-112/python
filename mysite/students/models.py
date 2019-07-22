from django.db import models

# Create your models here.

class Students(models.Model):
	full_name = models.CharField(max_length = 70)

	def __str__(self):
		return self.full_name

class StudentInfo(models.Model):
	name = models.ForeignKey(Students, on_delete = models.CASCADE) 
	gender = models.CharField(max_length = 10)
	standard = models.IntegerField(default = 0)
	division = models.CharField(max_length = 1)

	def __str__(self):
		return self.gender
