from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UsuarioNuevo(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Ingrese contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita su contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
        help_text = {k:"" for k in fields}
        
class TrabajadorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    puesto = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    email = forms.EmailField()
    
class EditUserForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Modificar Nombre")
    last_name = forms.CharField(label="Modificar Apellido")
    
    class Meta:
        model = User
        fields = ["email", "password1","password2", "first_name", "last_name"]
        help_texts = {k: "" for k in fields}
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Imagen")