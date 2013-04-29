"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from wia_db.models import WIAUser, WIAUserSkill
from wia_db.persistence import createUser
import pdb

class SimpleTest(TestCase):


    def test_persistence(self):
        users = WIAUser.objects.all()
        print(users)
        nu = WIAUser(first_name="Boda", last_name="da Silva", username="boda", user_type="boss", avatar_uri="http://boda.com")
        print(createUser(nu))
