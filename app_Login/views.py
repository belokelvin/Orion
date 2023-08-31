from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from pymongo import MongoClient
from .models import Usuario, MongoConnection

def home(request):
    return render(request, 'usuarios/home.html')

def go_cadastrar(request):
    return render(request, 'usuarios/Cadastro.html')

def go_login(request):
    return render(request, 'usuarios/Login.html')

def cadastro(request):
    print("Entrou")
    var_ClienteConection = MongoConnection()  # Correção do operador de atribuição
    var_db = var_ClienteConection.db  # Acessar o banco de dados da conexão

    usuarios_collection = var_db['Usuarios']

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Verificar se o usuário já existe no MongoDB
        if usuarios_collection.find_one({'username': username}):
            return redirect('home')  # Usuário já existe, redirecionar para a página inicial

        # Verificar se o usuário já existe no model do Django
        if Usuario.objects.filter(username=username).exists():
            return redirect('home')  # Usuário já existe, redirecionar para a página inicial

        # Inserir novo usuário no MongoDB
        usuarios_collection.insert_one({'username': username, 'password': password})

        # Hash da senha antes de inserir no model do Django
        hashed_password = make_password(password)
        novo_usuario = Usuario(username=username, password=hashed_password)
        novo_usuario.save()

        return redirect('pagina_carregar')  # Redirecionar para a página de carregamento

    return render(request, 'usuarios/Cadastro.html')
