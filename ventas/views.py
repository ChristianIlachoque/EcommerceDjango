from django.shortcuts import render, get_object_or_404


from .models import Venta
from .forms import VentaForm
# Create your views here.

def verVentaView(request, id):
    venta = Venta.objects.get(id = id)
    #form = ProductoForm(request.POST or None, instance=producto)

    # if form.is_valid():
    #     form.save()
    #     form = ProductoForm()

    context = {
        # 'form': form
        'venta': venta
    }

    return render(request, 'ventas/verVenta.html', context)

def crearVentaView(request):
    form = VentaForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = VentaForm()

    context = {
        'form': form
    }

    return render(request, 'ventas/crearVenta.html', context)

def editarVentaView(request, id):
    venta = Venta.objects.get(id = id)
    form = VentaForm(request.POST or None, instance=venta)

    if form.is_valid():
        form.save()
        form = VentaForm()

    context = {
        'form': form
    }

    return render(request, 'ventas/editarVenta.html', context)

def eliminarVentaView(request, id):
    venta = get_object_or_404(Venta, id = id)

    if request.method == 'POST':
        print("borrado ID:", id)
        venta.delete()

    context = {
        'venta': venta
    }

    return render(request, 'ventas/eliminarVenta.html', context)

def listaVentasView(request):
    listaVentas = Venta.objects.all()
    
    context = {
        'listaVentas': listaVentas
    }

    return render(request, 'ventas/listaVentas.html', context)