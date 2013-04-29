# WIA persistence API
from django.db.utils import DatabaseError

def createWIAObject(new_obj):
    try:
        if new_obj is not None:
            new_obj.save()
            return True
        else: 
            return False     
           
    except DatabaseError as e:
        print(e.strerror)
    
