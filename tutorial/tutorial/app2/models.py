from __future__ import unicode_literals

from django.db import models

LEVEL_CHOICES = ('EASY','easy'),('MEDIUM','medium'),('HARD','hard')

# Create your models here.
class Question(models.Model):
	description = models.CharField(max_length=100, blank=True, default='')
	level = models.CharField(choices=LEVEL_CHOICES, default='EASY', max_length=100)
	solution=models.CharField(max_length=5,blank=False, default='')
	def __str__(self):
		return self.description
    