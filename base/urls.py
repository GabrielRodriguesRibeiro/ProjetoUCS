from . import views
from django.urls import path

urlpatterns = [
    path('', views.principal, name="Principal"),
    path('adicionar/', views.adicionarItem, name="Adicionar")
]
