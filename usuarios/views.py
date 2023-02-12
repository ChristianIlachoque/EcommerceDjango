from django.shortcuts import render, get_object_or_404, redirect

#to authenticaded
from django.contrib.auth import authenticate, login, logout

from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def login(request):
    nombre = request.POST['nombre']
    clave = request.POST['clave']

    user = authenticate(request, nombre=nombre, clave=clave)

    if user is not None:
        login(request, user)
    else:
        return redirect('usuarios/login.html')

    #idk
    return render(request, "usuarios/login.html")

def logout(request):
    logout(request)
    
    return redirect("usuarios/login.html")

def register(request):
    return render(request, "usuarios/register.html")

def verUsuarioView(request, id):
    usuario = Usuario.objects.get(id = id)
    #form = ProductoForm(request.POST or None, instance=producto)

    # if form.is_valid():
    #     form.save()
    #     form = ProductoForm()

    context = {
        # 'form': form
        'usuario': usuario
    }

    return render(request, 'usuarios/verUsuario.html', context)

def crearUsuarioView(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = UsuarioForm()

    context = {
        'form': form
    }

    return render(request, 'usuarios/crearUsuario.html', context)

def editarUsuarioView(request, id):
    usuario = Usuario.objects.get(id = id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        form = UsuarioForm()

    context = {
        'form': form
    }

    return render(request, 'usuarios/editarUsuario.html', context)

def eliminarUsuarioView(request, id):
    usuario = get_object_or_404(Usuario, id = id)

    if request.method == 'POST':
        print("borrado ID:", id)
        usuario.delete()

    context = {
        'usuario': usuario
    }

    return render(request, 'usuarios/eliminarUsuario.html', context)

def listaUsuariosView(request):
    listaUsuarios = Usuario.objects.all()
    
    context = {
        'listaUsuarios': listaUsuarios
    }

    return render(request, 'usuarios/listaUsuarios.html', context)