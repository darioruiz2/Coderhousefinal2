from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

user = settings.AUTH_USER_MODEL

class Mensajeria(models.Model):
    enviar = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enviado")
    recibir = models.ForeignKey(User, on_delete=models.CASCADE, related_name="para")
    mensaje = models.TextField(max_length=500)
    horario = models.DateTimeField(auto_now_add=True)
    visto = models.BooleanField(default=False)
    
    def __str__(self):
        return f"De: {self.enviar} / PARA: {self.recibir} / MENSAJE: {self.mensaje} / HORA:{self.horario} / Visto: {self.visto}"
    

