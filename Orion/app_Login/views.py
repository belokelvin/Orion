from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages


from pymongo import MongoClient
from .models import Usuario, MongoConnection

def home(request):
    return render(request, 'usuarios/home.html')

def go_cadastrar(request):
    return render(request, 'usuarios/Cadastro.html')

def go_login(request):
    return render(request, 'usuarios/Login.html')

def cadastro(request):
    if request.method == 'POST':
        var_objConector = MongoConnection()
        var_objNovoUsuario = Usuario(var_objConector)
        var_strResultado = var_objNovoUsuario.create_user(request.POST.get('usuario'), request.POST.get('senha'))
        
        if var_strResultado == 'Usuário criado com sucesso!':
            messages.success(request, var_strResultado)  # Define a mensagem de sucesso usando o mecanismo de sessão
            return redirect('home')  # Redireciona de volta à página inicial