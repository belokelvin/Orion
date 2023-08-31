from django.urls import path
from app_Login import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/cadastrar/', views.go_cadastrar, name='go_cadastrar'),
    path('usuarios/cadastro/', views.cadastro, name='cadastro'),  # Correção no caminho
    path('usuarios/login/', views.go_login, name='go_login'),
]
