from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse   

# Create your models here.

class Post(models.Model):

	# this will be our data base having the field we want 
	# for our database system. 
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	# auto now = pdates the value of field to current time 
	#					and date every time the Model.save() is called.
	# auto now add =d - updates the value with 
						# the time and date of creation of record.


	#many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.
	#To create a recursive relationship – an object that has a many-to-one relationship with itself – 
	#use models.ForeignKey('self', on_delete=models.CASCADE).


	author = models.ForeignKey(User ,on_delete = models.CASCADE)

	#https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django
	def __str__(self):
		return self.title

	# here we just need to   handel create post working , 
	# and use the url to set that specific route
	# the reverse function is used for that purpose bt redirect would have done that
	# but reverse function just make that url as stirng and rest part
	# handel by the views #  
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):


	text_comment = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User ,on_delete = models.CASCADE)

	def __str__(self):
		return self.text_comment