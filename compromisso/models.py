from django.db import models
from django.utils import timezone
import datetime

class Compromisso(models.Model):
	descricao = models.TextField()
	horario = models.DateTimeField() # default=timezone.now
	local = models.TextField()
	
	def __str__(self):
		return self.descricao

class Observacoes(models.Model):
	observacao = models.TextField()
	fk_observacao = models.ForeignKey(Compromisso, on_delete=models.CASCADE)

	def __str__(self):
		return self.observacao