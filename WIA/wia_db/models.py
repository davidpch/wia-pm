from django.db import models

# WIA model
class WIAUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    user_type = models.CharField(max_length=50)
    avatar_uri = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.username
    
    def __str__(self):
        return self.username
    
class WIAUserSkill(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(WIAUser)
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title    
    
class ActionLog(models.Model):
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(WIAUser)
    
    def __unicode__(self):
        return self.description
    
    def __str__(self):
        return self.description    

class Project(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    users = models.ManyToManyField(WIAUser)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
        
class Template(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name    
    
class Phase(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name    
    
class Milestone(models.Model):
    name = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    phase = models.ForeignKey(Phase)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name    
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=30)
    priority = models.IntegerField()
    total_time = models.IntegerField()
    phase = models.ForeignKey(Phase)
    users = models.ManyToManyField(WIAUser) #users associated with task/subtask
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title    
            
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
    
    def __unicode__(self):
        return self.text
    
    def __str__(self):
        return self.text    
    
class CodeLink(models.Model):
    code_url = models.URLField()
    revision = models.IntegerField()
    parent_task = models.ForeignKey(Subtask)
    
    def __unicode__(self):
        return self.code_url
    
    def __str__(self):
        return self.code_url    
    
class Event(models.Model):
    timestamp = models.DateTimeField()
    class Meta:
        abstract = True
        
class Colision(Event):
    message = models.CharField(max_length=500)
    parent_task = models.ForeignKey(Task)
    
    def __unicode__(self):
        return self.message
    
    def __str__(self):
        return self.message    
    
class Flag(Event):
    message = models.CharField(max_length=500)
    parent_task = models.ForeignKey(Task)    
    
    def __unicode__(self):
        return self.message
    
    def __str__(self):
        return self.message      

class Prediction(models.Model):
    
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField()
    project = models.ForeignKey(Project)
    users = models.ForeignKey(WIAUser)
    
    def __unicode__(self):
        return self.message
    
    def __str__(self):
        return self.message      
    
        