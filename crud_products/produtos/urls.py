from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.novo_produto, name='novo_produto'),
    path('edita/<str:codigo>/', views.edita_produto, name='edita_produto'),
    path('excluir/<str:codigo>/', views.exclui_produto, name='exclui_produto'),
]