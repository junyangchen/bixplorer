from django.db import models
from django.contrib.auth.models import User

class DataSet(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.name
    
# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User)
    dataset = models.ForeignKey(DataSet)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    create_time = models.DateTimeField('date published')
    is_private = models.BooleanField(default = 1)
    is_deleted = models.BooleanField(default = 0)
    def __unicode__(self):
        return self.name   
        
    def is_creator(self, user):
        return user == self.user #or user.has_perm('your_app.manage_object')
    
class Comment(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=500)    
    create_time = models.DateTimeField('date published')
    is_deleted = models.BooleanField(default = 0)
    
    def __unicode__(self):
        return self.content   
    
    def is_comment_creator(self, user):
        return user == self.user
        
    def is_project_creator(self, user):
        return user == self.project.user
       