from django.db import models

# Create your models here.
class WIAUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    avatar_uri = models.CharField(max_length=200)
    
class WIAUserSkill(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(WIAUser)
    
class ActionLog(models.Model):
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(WIAUser)

class Project(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    users = models.ManyToManyField(WIAUser)
    
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
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=30)
    priority = models.IntegerField()
    total_time = models.IntegerField()
            
class Subtask(Task):    
    code_level = models.IntegerField()
    parent_task = models.ForeignKey(Task, related_name='parent')

class QASubtask(Subtask):
    bug_notes = models.CharField(max_length=500)
    recheck = models.BooleanField()
    resolved = models.BooleanField()

class Comment(models.Model):
    text = models.CharField(max_length=500)
    parent_task = models.ForeignKey(Task)
    
class CodeLink(models.Model):
    code_url = models.URLField()
    revision = models.IntegerField()
    parent_task = models.ForeignKey(Subtask)
    
class Event(models.Model):
    timestamp = models.DateTimeField()
    class Meta:
        abstract = True
        
class Colision(Event):
    message = models.CharField(max_length=500)
    parent_task = models.ForeignKey(Task)
    
class Flag(Event):
    message = models.CharField(max_length=500)
    parent_task = models.ForeignKey(Task)    

class Prediction(models.Model):
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    project = models.ForeignKey(Project)
    users = models.ForeignKey(WIAUser)
    
        