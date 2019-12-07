from django import forms

from .models import Sugestoes

class SugestoesForm(forms.ModelForm):

    #O formulario vai receber o modelo Sugestoes, com seus atributos titulo e comentarios
    class Meta:
        model = Sugestoes
        fields = ('titulo','comentarios')

#class DenunciasForm(forms.ModelForm):
    
 #   class Meta:
 #       model = Denuncias
 #       fields = ('titulo','comentarios')

#class ReclamacoesForm(forms.ModelForm):
    
 #   class Meta:
 #       model = Reclamacoes
 #       fields = ('titulo','comentarios')

#class ElogiosForm(forms.ModelForm):
    
 #   class Meta:
 #       model = Elogios
 #       fields = ('titulo','comentarios')

#class NameForm(forms.Form):
 #   your_name = forms.CharField(label='Your name', max_length=100)
