from django.db import models

# Create your models here.
class WIAUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    avatar_uri = models.CharField(max_length=200)

class Project(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    
class Template(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)
    
class Phase(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    project = models.ForeignKey(Project)
    
class Milestone(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    phase = models.ForeignKey(Phase)
    
class Comment(models.Model):
    text = models.CharField(max_length=300)
    
class AbstractTask(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=30)
    priority = models.IntegerField()
    code_level = models.IntegerField()
    total_time = models.IntegerField()
    class Meta:
        abstract = True
        
class Task(AbstractTask):
    
    
        