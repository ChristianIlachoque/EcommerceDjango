from django.shortcuts import render, get_object_or_404


from .models import Producto
from .forms import ProductoForm
# Create your views here.

def verProductoView(request, id):
    producto = Producto.objects.get(id = id)
    #form = ProductoForm(request.POST or None, instance=producto)

    # if form.is_valid():
    #     form.save()
    #     form = ProductoForm()

    context = {
        # 'form': form
        'producto': producto
    }

    return render(request, 'templates/productos/verProducto.html', context)

def crearProductoView(request):
    form = ProductoForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductoForm()

    context = {
        'form': form
    }

    return render(request, 'productos/crearProducto.html', context)

def editarProductoView(request, id):
    producto = Producto.objects.get(id = id)
    form = ProductoForm(request.POST or None, instance=producto)

    if form.is_valid():
        form.save()
        form = ProductoForm()

    context = {
        'form': form
    }

    return render(request, 'productos/editarProducto.html', context)

def eliminarProductoView(request, id):
    producto = get_object_or_404(Producto, id = id)

    if request.method == 'POST':
        print("borrado ID:", id)
        producto.delete()

    context = {
        'producto': producto
    }

    return render(request, 'productos/eliminarProducto.html', context)

def listaProductosView(request):
    listaProductos = Producto.objects.all()
    
    context = {
        'listaProductos': listaProductos
    }

    return render(request, 'productos/listaProductos.html', context)