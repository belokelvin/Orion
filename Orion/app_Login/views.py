from django.shortcuts import render, redirect

def home(request):
    return render(request, 'usuarios/home.html')

def go_cadastrar(request):
    return render(request, 'usuarios/Cadastro.html')

def go_login(request):
    return render(request, 'usuarios/Login.html')