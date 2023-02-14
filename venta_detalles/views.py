from django.shortcuts import render, get_object_or_404


from .models import VentaDetalles
from .forms import VentaDetallesForm
# Create your views here.

def verVentaDetallesView(request, id):
    venta_detalles = VentaDetalles.objects.get(id = id)
    #form = ProductoForm(request.POST or None, instance=producto)

    # if form.is_valid():
    #     form.save()
    #     form = ProductoForm()

    context = {
        # 'form': form
        'venta_detalles': venta_detalles
    }

    return render(request, 'venta_detalles/verVentaDetalles.html', context)

def crearVentaDetallesView(request):
    form = VentaDetallesForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = VentaDetallesForm()

    context = {
        'form': form
    }

    return render(request, 'venta_detalles/crearVentaDetalles.html', context)

def editarVentaDetallesView(request, id):
    venta_detalles = VentaDetalles.objects.get(id = id)
    form = VentaDetallesForm(request.POST or None, instance=venta_detalles)

    if form.is_valid():
        form.save()
        form = VentaDetallesForm()

    context = {
        'form': form
    }

    return render(request, 'venta_detalles/editarVentaDetalles.html', context)

def eliminarVentaDetallesView(request, id):
    venta_detalles = get_object_or_404(VentaDetalles, id = id)

    if request.method == 'POST':
        print("borrado ID:", id)
        venta_detalles.delete()

    context = {
        'venta_detalles': venta_detalles
    }

    return render(request, 'venta_detalles/eliminarVentaDetalles.html', context)

def listaVentasDetallesView(request):
    listaVenta_Detalles = VentaDetalles.objects.all()
    
    context = {
        'listaVenta_Detalles': listaVenta_Detalles
    }

    return render(request, 'venta_detalles/listaVentaDetalles.html', context)