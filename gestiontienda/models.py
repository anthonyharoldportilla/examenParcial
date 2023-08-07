from django.db import models

# Create your models here.

class tienda(models.Model):
    direccion=models.CharField(max_length=64, blank=True, null=True)
    provincia=models.CharField(max_length=32, blank=True, null=True)
    region=models.CharField(max_length=32, blank=True, null=True)
    fechaCreacion=models.CharField(max_length=32, blank=True, null=True)
    telefonoContacto=models.CharField(max_length=32, blank=True, null=True)



class producto(models.Model):
    descripcion=models.CharField(max_length=64, blank=True, null=True)
    codigo=models.CharField(max_length=32, blank=True, null=True)
    precioVenta=models.CharField(max_length=32, blank=True, null=True)
    cantidad=models.CharField(max_length=32, blank=True, null=True)
    tiendaProducto = models.ForeignKey(tienda,on_delete=models.SET_NULL,blank=True, null=True)
    #productoTienda = models.OneToOneField(tienda, on_delete=models.SET_NULL, blank=True, null=True)


