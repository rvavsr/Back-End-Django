from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/novo/', views.criar_cliente, name='criar_cliente'),
    path('clientes/<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/remover/', views.remover_cliente, name='remover_cliente'),

    path('vendas/', views.listar_vendas, name='listar_vendas'),
    path('vendas/novo/', views.criar_venda, name='criar_venda'),           # <<< Adicionei aqui
    path('vendas/<int:pk>/editar/', views.editar_venda, name='editar_venda'),  # <<< e aqui
    path('vendas/<int:pk>/remover/', views.remover_venda, name='remover_venda'), # <<< e aqui

    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('produtos/<int:id>/editar/', views.produto_update, name='produto_update'),
    path('produtos/<int:id>/excluir/', views.produto_delete, name='produto_delete'),
]
