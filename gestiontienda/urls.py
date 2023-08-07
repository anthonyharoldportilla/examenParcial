from django.urls import path
from  . import views

app_name='gestiontienda'

urlpatterns=[
    path('',views.index,name='index'),
    path('tiendas',views.registroTienda,name='registroTienda'),
    path('productos',views.registroProducto,name='registroProducto'),
    path('eliminarProducto/<str:idProducto>', views.eliminarProducto,name='eliminarProducto'),
    path('eliminarTienda/<str:idTienda>', views.eliminarTienda,name='eliminarTienda'),
    path('asignarProducto',views.asignarProducto,name='asignarProducto'),
    path('verProductos/<str:idTienda>',views.verProductos,name='verProductos')
    
]