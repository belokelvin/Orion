from django.db import models
import pymongo
from django.contrib.auth.hashers import make_password

class MongoConnection:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb+srv://kelvincrdzbl:535846*Mud@machosbd.jrrfws5.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client['Machos']
        self.users_collection = self.db["Usuarios"]

class Usuario(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

