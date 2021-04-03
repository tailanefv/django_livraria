from django import forms

from livraria.models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('nome','autor','categoria','codigo', 
        'quantidade', 'valor', 'imagem', 'ano', 'descricao')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Ex: Redes de Computadores'}),
            'autor': forms.SelectMultiple(attrs={ 'class': 'form-control'}),
            'categoria': forms.Select(attrs={ 'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'Ex: 101010'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'Ex: 200'}),
            'valor': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'Ex: 400'}),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control'}),
            'ano': forms.TextInput(attrs={ 'class': 'form-control',
                                            'placeholder':'Ex: 2021'}),
            'descricao': forms.Textarea(attrs={ 'class': 'form-control'}),
        }