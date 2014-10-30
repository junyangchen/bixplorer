from django.db import models
from django.contrib.auth.models import User

class DataSet(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField('date published')
    
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User)
    dataset = models.ForeignKey(DataSet)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    create_time = models.DateTimeField('date published')
    
class Comment(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=500)
    
    create_time = models.DateTimeField('date published')
    