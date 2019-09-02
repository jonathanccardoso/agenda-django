from django.shortcuts import render
from .models import Compromisso

def index(request):
    compromissos_list = Compromisso.objects.order_by('-data')
    context = {'compromissos_list': compromissos_list}
    return render(request, 'compromisso/index.html', context)
