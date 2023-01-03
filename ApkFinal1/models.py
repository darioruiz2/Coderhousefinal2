from django.db import models
from django.contrib.auth.models import User

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} / Apellido: {self.apellido} / Puesto:{self.puesto} / Edad:{self.edad} / Email:{self.email}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"