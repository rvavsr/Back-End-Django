from django.contrib import admin

from django.contrib import admin
from .models import Produto, Cliente, Venda

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Venda)
