############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """
import sys
import os
import django

# Turn off bytecode generation
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

# Import your models for use in your script
from db.models.user import User

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
User.objects.create(name='Dan')
User.objects.create(name='Robert')

for u in User.objects.all():
    print(f'ID: {u.id} \tUsername: {u.name}')
