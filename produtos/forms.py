from django import forms
from .models import Cliente, Venda, Produto  # <-- adicione Produto aqui

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'

class ProdutoForm(forms.ModelForm):   # <-- novo form para Produto
    class Meta:
        model = Produto
        fields = '__all__'
