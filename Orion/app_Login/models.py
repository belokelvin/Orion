from django.db import models
import pymongo
from django.contrib.auth.hashers import make_password

class MongoConnection:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb+srv://kelvincrdzbl:535846*Mud@machosbd.jrrfws5.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client['Machos']
        self.users_collection = self.db["Usuarios"]

class User:
    def __init__(self, mongo_connection):
        self.mongo_connection = mongo_connection
        
    def create_user(self, Usuario, Senha):
        try:
            hashed_password = make_password(Senha)  # Hasheie a senha
            self.mongo_connection.users_collection.insert_one({"Usuario": Usuario, "Senha": hashed_password})
            return "Usuário criado com sucesso!"
        except pymongo.errors.DuplicateKeyError:
            return "Nome de usuário já existe."

