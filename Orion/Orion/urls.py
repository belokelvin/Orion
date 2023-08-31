from django.urls import path
from app_Login import views


urlpatterns = [
    path('', views.home, name='home'),
    # Adicione esta linha para a página de boas-vindas
]