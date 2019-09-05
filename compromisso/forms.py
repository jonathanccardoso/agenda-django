from django import forms
from .models import Observacoes

class ObservacoesForm(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = ('observacao', )