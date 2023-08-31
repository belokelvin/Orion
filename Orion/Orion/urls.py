from django.urls import path
from app_Login import views


urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.go_cadastrar, name='go_cadastrar'),
    path('usuarios/', views.go_login, name='go_login'),
    # Adicione esta linha para a página de boas-vindas
]