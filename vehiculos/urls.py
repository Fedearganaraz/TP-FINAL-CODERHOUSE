from django.urls import path
from .views import home, ListarLibro, CrearLibro, EditarLibro, MostarLibro, EliminarLibro
from vehiculos import views
from vehiculos import Templates



urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('saludos/', views.saludar),
    path('estatico/', views.crear_estatico),
    path('mostrar/', views.mostrar, name = "mostrar"),
    path('dinamico/', views.crear_dinamico, name = "crear"),
    path('detail_<int:id>/', views.detail, name="detalles"),
    path('editar_<int:id2>/', views.actualizar, name="actualizar"),
    path('borrar_<int:id2>', views.borrar, name="borrar"),
    path('CRUD/', views.CRUD, name="CRUD"),
    path('buscador/', views.buscar),
    path('', home, name="inicio" ),
    path('libros/', ListarLibro.as_view(), name="listar_libro"),
    path('crear_libro/', CrearLibro.as_view(), name="crear_libro"),
    path('editar_libro/', EditarLibro.as_view(), name="editar_libro"),
    path('mostrar_libro/', MostarLibro.as_view(), name="mostrar_libro"),
    path('eliminar_libro/', EliminarLibro.as_view(), name="eliminar_libro"),
    
]
