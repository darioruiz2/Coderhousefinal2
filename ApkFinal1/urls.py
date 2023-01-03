from django.urls import path
from ApkFinal1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("padre/", views.padre, name = "padre" ),
    path("AcercaDeMi/", views.AcercaDeMi, name = "AcercaDeMi"),
    path("Login/", views.Login_request, name = "Login"),
    path("Inicio/", views.Vistainicio, name = "Inicio1"),
    path("Registro/", views.Registro, name = "Registro"),
    path("logout/", LogoutView.as_view(), name = "Logout"),
    path("Noencontrada/", views.Noencontrada, name = "Noencontrada"),
    path("Trabajador/", views.Trabajador1, name = "Trabajador"),
    path("Usuarioedit/", views.Usuarioedit, name = "Usuarioedit" ),
    path("VerTrabajadores", views.VistaTrabajadores, name = "Viewtrabajadores"),
    path("Trabajadoredit/<id>", views.EditTrabajadores, name = "Trabajadoredit"),
    path("TrabajadorDelete/<id>", views.DeleteTrabajadores, name = "TrabajadorDelete"),
    path("Avataredit/", views.AvatarEdit, name = "Avataredit"),
    path("Usuarios/", views.VistaUsuarios, name = "Usuarios"),
    path("Deleteuser/<int:user_id>", views.DeleteUser, name = "Deleteuser"),
]
