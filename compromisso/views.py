from django.shortcuts import render, get_object_or_404
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Compromisso, Observacoes
from .forms import ObservacoesForm

def index(request):
    compromissos_list = Compromisso.objects.order_by('-horario')[:20];
    data_hoje = datetime.now()
    context = {'compromissos_list': compromissos_list, 'data_hoje': data_hoje}
    return render(request, 'compromisso/index.html', context)

def detalhe(request, compromisso_id):

    compromisso = get_object_or_404(Compromisso, pk=compromisso_id)

    form = ObservacoesForm()
    
    if request.method == "POST":            
        form = ObservacoesForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.fk_observacao = compromisso
            form.save()

    observacoes = list(Observacoes.objects.filter(fk_observacao=compromisso_id))

    context = {
        'observacoes': observacoes,
        'form': form,
    }

    return render(request, 'compromisso/detalhe.html', context)
