from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from pymongo import MongoClient
from .models import Usuario, MongoConnection
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request, 'usuarios/home.html')

def go_dash(request):
    return render(request, 'usuarios/logado.html')


def go_cadastrar(request):
    return render(request, 'usuarios/Cadastro.html')

def go_login(request):
    return render(request, 'usuarios/Login.html')

def cadastro(request):
    if request.method == 'POST':
        var_objConector = MongoConnection()
        var_objNovoUsuario = Usuario(var_objConector)
        print(request.POST.get('username'))
        var_strResultado = var_objNovoUsuario.create_user(request.POST.get('username'), request.POST.get('senha'))
        
        if var_strResultado == 'Usuário criado com sucesso!':
            messages.success(request, var_strResultado)  # Define a mensagem de sucesso usando o mecanismo de sessão
            return redirect('home')  # Redireciona de volta à página inicial

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        var_objConector = MongoConnection()
        user = var_objConector.users_collection.find_one({"Usuario": username})
        print(user)
        print(make_password(password))
        print(password)
        if user and check_password(password, user['Senha']):
            print('a')
            request.session['Usuario'] = user['Usuario']
            request.session.set_expiry(7200)
            messages.success(request, 'Login realizado com sucesso')
            return render(request, 'usuarios/logado.html')
        else:
            print('b')
            messages.error(request, 'Credenciais inválidas')
            return render(request, 'usuarios/Login.html')