from django.db import models
from django.utils import timezone
import datetime

class Compromisso(models.Model):
	descricao = models.TextField()
	horario = models.DateTimeField() # default=timezone.now
	local = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.descricao
