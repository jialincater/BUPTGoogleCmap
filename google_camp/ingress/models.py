from django.db import models

# Create your models here.
class Agent(models.Model):
	name = models.CharField(max_length=10,primary_key=True)
	level = models.IntegerField()
	mail = models.EmailField(default="hi@hi.hi")
	phone = models.IntegerField(default=10086)
	eat = models.BooleanField(default=False)
	password = models.CharField(default="",max_length=100)
	join = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name