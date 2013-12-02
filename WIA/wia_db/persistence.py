# WIA persistence API
from django.db.utils import DatabaseError
from wia_db.models import WIAUser, Subtask, Project, Prediction

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
        
    
def getPredictionFromUser(usr):
    """
    Gets the list of predictions related with the user
    """
    return Prediction.objects.filter(users__id=usr.id)


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
    
    
        
    
    
