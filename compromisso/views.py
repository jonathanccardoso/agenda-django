from django.shortcuts import render
from datetime import datetime
from .models import Compromisso

def index(request):
    compromissos_list = Compromisso.objects.order_by('-horario')
    data_hoje = datetime.now()
    context = {'compromissos_list': compromissos_list, 'data_hoje': data_hoje}
    return render(request, 'compromisso/index.html', context)
