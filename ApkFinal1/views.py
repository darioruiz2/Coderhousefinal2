from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import TrabajadorForm, UsuarioNuevo, EditUserForm, AvatarForm
from .models import Trabajador, Avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




@login_required
def Usuarioedit(request):
    usuario1 = request.user
    if request.method == "POST":
        form = EditUserForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario1.email = info["email"]
            usuario1.password1 = info["password1"]
            usuario1.password2 = info["password2"]
            usuario1.first_name = info["first_name"]
            usuario1.last_name = info["last_name"]
            usuario1.save()
            return render(request, "AppCoder/Inicio.html", {"mensaje1":"Perfil editado correctamente"})
        else:
            return render(request, "AppCoder/Usuarioedit.html", {"mensaje1": "Error al editar perfil"})
    else:
         form = EditUserForm(instance = usuario1)
    return render(request, "AppCoder/Usuarioedit.html", {"form":form, "nombreusuario": usuario1.username,"imagen":ObtenerImagen(request) })


def Trabajador1(request):
    if request.method == "POST":
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            puesto = info["puesto"]
            edad = info["edad"]
            email = info["email"]
            
            guardar1 = Trabajador(nombre = nombre, apellido = apellido, puesto = puesto, edad = edad, email = email)
            guardar1.save()
            return render(request, "AppCoder/Inicio.html",{"mensaje": "Trabajador creado con exito"})
        else:
            return render(request, "AppCoder/Trabajador.html", {"mensaje": "Error al crear trabajador."})
    else:
        form = TrabajadorForm()        
    return render(request, "AppCoder/Trabajador.html",{"form": form,"imagen":ObtenerImagen(request) })

def AvatarEdit(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            AvatarViejo = Avatar.objects.filter(user = request.user)
            if len(AvatarViejo) != 0:
                AvatarViejo[0].delete()
            avatar1 = Avatar(user = request.user, imagen = request.FILES["imagen"])
            avatar1.save()
            return render(request, "AppCoder/Inicio.html", {"mensaje3": "Avatar agregado correctamente."})
        else:
            return render(request, "AppCoder/Avataredit.html",{"mensaje3": "Error al modificar avatar.", "usuario": request.user})
    else:
        form = AvatarForm()
        return render(request, "AppCoder/Avataredit.html", {"form1": form, "usuario": request.user, "imagen":ObtenerImagen(request)})
    

def Noencontrada(request):
    return render(request, "AppCoder/Noencontrada.html")

def padre(request):
    return render(request, "AppCoder/padre.html")

@login_required
def AcercaDeMi(request):
    return render(request,"AppCoder/AcercaDeMi.html", {"imagen": ObtenerImagen(request)})

@login_required
def Vistainicio(request):
    
    return render(request, "AppCoder/Inicio.html", {"imagen": ObtenerImagen(request)})

def ObtenerImagen(request):
    lista = Avatar.objects.filter(user = request.user)
    if len(lista) !=0:
        imagen = lista[0].imagen.url
    else:
         imagen = "/media/avatares/avatarpredeterminado.png"
    return imagen

def Login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            usuario1 = authenticate(username = usu, password = clave)#trae un usuario de la base
            if usuario1 is not None:
                login(request, usuario1)
                return render(request, "AppCoder/Login.html",{"mensaje": (f"BIENVENIDO!,Usuario : {usuario1}")})
            else:
                return render(request,"AppCoder/Login.html", {"mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/Login.html",{"mensaje": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
         
    return render(request, "AppCoder/Login.html",{"form": form })

def Registro(request):
    if request.method == "POST":
        form = UsuarioNuevo(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "AppCoder/Login.html", {"mensaje": (f"Usuario {username} creado correctamente")})
        else:
            return render(request, "AppCoder/Registro.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form= UsuarioNuevo()
    return render(request, "AppCoder/Registro.html", {"form": form})

@login_required
def VistaTrabajadores(request):
    
    trabajadores = Trabajador.objects.all()
    
    return render(request, "AppCoder/Viewtrabajadores.html",{"trabajadores": trabajadores, "imagen":ObtenerImagen(request)})



@login_required
def EditTrabajadores(request, id):
    trabajador = Trabajador.objects.get(id = id)
    if request.method == "POST":
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            trabajador.nombre = info["nombre"]
            trabajador.apellido = info["apellido"]
            trabajador.puesto = info["puesto"]
            trabajador.edad = info["edad"]
            trabajador.email = info["email"]
            trabajador.save()
            return render(request, "AppCoder/Viewtrabajadores.html",{"mensaje2": "trabajador editado correctamente"})
        else:
            return render(request, "AppCoder/Trabajadoredit.html", {"mensaje2": "Error al editar trabajador"})
    else:
        formulario = TrabajadorForm(initial={"nombre":trabajador.nombre, "apellido": trabajador.apellido, "puesto": trabajador.puesto, "edad": trabajador.edad, "email": trabajador.edad})
    return render(request, "AppCoder/Trabajadoredit.html",{"form": formulario, "trabajador":trabajador,"imagen":ObtenerImagen(request)})

@login_required
def DeleteTrabajadores(request,id):
    trabajador = Trabajador.objects.get(id = id)
    trabajador.delete()
    
    trabajadores = Trabajador.objects.all()
    
    ctx = {"trabajadores":  trabajadores}
    return render(request, "AppCoder/Viewtrabajadores.html", ctx)

@login_required
def DeleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    
    user.delete()
    
    return render(request,"AppCoder/Login.html", {"mensaje001": "Usuario eliminado"})
    

def VistaUsuarios(request):
    return render(request, "AppCoder/Usuarios.html")





