# WIA persistence API
from django.db.utils import DatabaseError
from wia_db.models import WIAUser, Subtask, Project

def createWIAObject(new_obj):
    try:
        if new_obj is not None:
            new_obj.save()
            return True
        else: 
            return False     
           
    except DatabaseError as e:
        print(e.__str__())
        
def updateWIAObject(obj):
    try:
        if obj is not None:
            obj.save()
            return True
        else: 
            return False     
           
    except DatabaseError as e:
        print(e.__str__())        
        

def createWIAUser(new_user):
    return createWIAObject(new_user)
    
    
def updateWIAUser(usr):
    return updateWIAObject(usr) 

def getWIAUser(usern):
    return WIAUser.objects.get(username=usern)
    
    
def createProject(new_proj):
    return createWIAObject(new_proj)
    
def updateProject(proj):
    return updateWIAObject(proj)
    
    
def createTask(new_task):
    return createWIAObject(new_task)

def updateTask(tsk):
    return updateWIAObject(tsk)

def createProjectPhase(ph):
    return createWIAObject(ph)

def updateProjectPhase(ph):
    return updateWIAObject(ph)

def createMilestone(ml):
    return createWIAObject(ml)

def updateMilestone(ml):
    return updateWIAObject(ml)

def createProjectTemplate(tmpl):
    return createWIAObject(tmpl)

def updateProjectTemplate(tmpl):
    return updateWIAObject(tmpl)

def insertUserLog(log):
    return createWIAObject(log)

def getProjectFromUser(usr):
    """
    Gets the list of projects in which the user is currently enrolled
    """
    return Project.objects.filter(users__id=usr.id)

def getSubTasksFromUser(usr, prj):
    """
    Gets all the subtasks from a user of a certain project
    usr - user to filter. 
    prj - project id to filter

    """
    return Subtask.objects.filter(phase__project__id=prj.id, users__id=usr.id)
    
    
        
    
    