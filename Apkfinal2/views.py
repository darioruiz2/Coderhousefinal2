from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def Padre(request):
    return render(request,"AppCoder/padre.html")

def Vistamensaje(request):
    return render(request,"AppCoder/Mensajeria.html")


@login_required
def MensajeFormulario(request):
    usuario1 = request.user
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            para1 = info["para"]
            texto = info["mensaje"]
            mensaje0 = Mensajeria(enviar = (usuario1), recibir = (para1), mensaje = texto, visto = False)
            mensaje0.save()
            return render(request, "AppCoder/Mensajeform.html", {"form":form, "mensaje1": "Mensaje Enviado"})
        else:
            return render(request, "AppCoder/Inicio1.html", {"mensaje1": "Error al enviar mensaje"})
    else:
        form = MensajeForm()
    return render(request, "AppCoder/Mensajeform.html", {"form": form})


@login_required
def Mensajeleer(request):
    usuario = request.user
    ayuda = Mensajeria.objects.filter(recibir = usuario)
    for mensaje in ayuda:
        mensaje.visto = True
        mensaje.save()
    
    return render(request, "AppCoder/Mensajeleer.html", {"mensajes": ayuda})


@login_required
def Mensajeenviado(request):
    usuario = request.user
    mensajes = Mensajeria.objects.filter(enviar = usuario)
    return render(request, "AppCoder/Mensajeenviado.html", {"mensajes": mensajes})

        