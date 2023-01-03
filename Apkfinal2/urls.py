from django.urls import path
from Apkfinal2 import views


urlpatterns = [
    path("Padre/", views.Padre, name = "Padre"),
    path("Mensajeria/", views.Vistamensaje, name = "Mensajeria"),
    path("Mensajeleer/", views.Mensajeleer, name = "Mensajeleer"),
    path("Mensajeform/", views.MensajeFormulario, name= "Mensajeform"),
    path("Mensajeenviado/", views.Mensajeenviado, name="Mensajeenviado"),
]
