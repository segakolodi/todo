from django.db import models

# Create your models here.
class todo(models.Model):
	# creating attributes
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.title


