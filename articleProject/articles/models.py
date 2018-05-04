from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length = 100)
	slug = models.SlugField()
	content = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	auther = models.ForeignKey(User, default=None)

def __str__(self):
	return self.title

def snippet(self):
	return self.content[:50]  + '....'	


class Comment(models.Model):
	userName = models.CharField(max_length = 20)
	email = models.EmailField()
	comment = models.TextField()
	posted = models.DateTimeField(auto_now_add = True)
	approved = models.BooleanField(default = False)
	articleName	= models.ForeignKey(Article, default = None)

def __str__(self):
	return self.userName

def approved(self):
	self.approved = True
	self.save()
