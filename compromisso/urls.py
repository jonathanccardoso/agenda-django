from django.urls import path, include

from . import views

app_name = 'compromisso'
urlpatterns = [
    path('', views.index, name='index'),
  	path('<int:compromisso_id>/', views.detalhe, name='detalhe'),
  	path('delete/<int:observacao_id>/', views.delete, name='delete'),
]
