from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import tienda ,producto

# Create your views here.
listaUsuario = []

def index(request):
     return render(request,'inicio.html')


def registroTienda(request):
    if request.method=='POST':
        tiendaDireccion= request.POST.get('tiendaDireccion')
        tiendaProvincia= request.POST.get('tiendaProvincia')
        tiendaRegion= request.POST.get('tiendaRegion')
        tiendaFechaCreacion= request.POST.get('tiendaFechaCreacion')
        tiendaTelefonoContacto= request.POST.get('tiendaTelefonoContacto')
        tienda.objects.create(
            direccion=tiendaDireccion,
            provincia=tiendaProvincia,
            region=tiendaRegion,
            fechaCreacion=tiendaFechaCreacion,
            telefonoContacto=tiendaTelefonoContacto
        )
        #listaUsuario.append([nombreUsuario,apellidoUsuario])
        return HttpResponseRedirect(reverse('gestiontienda:registroTienda'))
    return render(request,'registroTienda.html',{
        'tiendaTotales':tienda.objects.all().order_by('id'),
         'productoTotales':producto.objects.all().order_by('id'),
    })


def registroProducto(request):
    if request.method=='POST':
        descripcion=request.POST.get('descripcionProducto')
        codigo=request.POST.get('codigoProducto')
        precioVenta=request.POST.get('precioventaProducto')
        cantidad=request.POST.get('cantidadProducto')
        producto.objects.create(
            descripcion=descripcion,
            codigo=codigo,
            precioVenta=precioVenta,
            cantidad=cantidad
        )
        return HttpResponseRedirect(reverse('gestiontienda:registroProducto'))
    return render(request,'registroProducto.html',{
        'productoTotales':producto.objects.all().order_by('id'),
        'tiendaTotales':tienda.objects.all().order_by('id')        
    })


def asignarProducto(request):
    if request.method == 'POST':
        idTienda= request.POST.get('tiendaSeleccionada')
        idProducto= request.POST.get('productoSeleccionado')
        objetoProducto=producto.objects.get(id=idProducto)
        objetoTienda=tienda.objects.get(id=idTienda)
        objetoProducto.tiendaProducto=objetoTienda
        objetoProducto.save()
        return HttpResponseRedirect(reverse('gestiontienda:registroTienda'))

def eliminarProducto(request,idProducto):
    productoEliminar= producto.objects.get(id=idProducto)
    productoEliminar.delete()
    return HttpResponseRedirect(reverse('gestiontienda:registroProducto'))

def eliminarProductoTienda(request,idProducto):
    productoEliminar= producto.objects.get(id=idProducto)
    productoEliminar.delete()
    return HttpResponseRedirect(reverse('gestiontienda:registroTienda'))

def eliminarTienda(request,idTienda):
    tiendaEliminar= tienda.objects.get(id=idTienda)
    tiendaEliminar.delete()
    return HttpResponseRedirect(reverse('gestiontienda:registroTienda'))


def  verProductos(request,idTienda):
    tiendaSeleccionada=tienda.objects.get(id=idTienda)   
    return render(request,'detalleTienda.html',{
      'infoproductosTiendas':tiendaSeleccionada.producto_set.all().order_by('id'),
      'tiendaSeleccionada':tiendaSeleccionada
      
    })
    

        


