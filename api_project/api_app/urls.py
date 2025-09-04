from django.urls import path
from .views import (
    AutorList, CrearAutor, ActualizarAutor, EliminarAutor, EditorialList, CrearEditorial, ActualizarEditorial, 
    EliminarEditorial, LibroList, CrearLibro, ActualizarLibro, EliminarLibro, MiembroList, CrearMiembro, ActualizarMiembro, 
    EliminarMiembro, PrestamoList, CrearPrestamo, ActualizarPrestamo, EliminarPrestamo, LibroByAutor, LibroByEditorial, PrestamoByFecha, PrestamoByMiembro,
    LibroByNoDevueltoRango
)

urlpatterns = [
    path('autores/', AutorList.as_view(), name='autores-list '),
    path('autores/crear/', CrearAutor.as_view(), name='autores-crear'),
    path('autores/actualizar/<int:pk>', ActualizarAutor.as_view(), name='autores-actualizar'),
    path('autores/eliminar/<int:pk>', EliminarAutor.as_view(), name='autores-eliminar'),
    path('editoriales/', EditorialList.as_view(), name='editoriales-list'),
    path('editoriales/crear/', CrearEditorial.as_view(), name='editoriales-crear'),
    path('editoriales/actualizar/<int:pk>', ActualizarEditorial.as_view(), name='editoriales-actualizar'),
    path('editoriales/eliminar/<int:pk>', EliminarEditorial.as_view(), name='editoriales-eliminar'),
    path('libros/', LibroList.as_view(), name='libros-list'),
    path('libros/crear/', CrearLibro.as_view(), name='libros-crear'),
    path('libros/actualizar/<int:pk>', ActualizarLibro.as_view(), name='libros-actualizar'),
    path('libros/eliminar/<int:pk>', EliminarLibro.as_view(), name='libros-eliminar'),
    path('miembros/', MiembroList.as_view(), name='miembros-list'),
    path('miembros/crear/', CrearMiembro.as_view(), name='miembros-crear'),
    path('miembros/actualizar/<int:pk>', ActualizarMiembro.as_view(), name='miembros-actualizar'),
    path('miembros/eliminar/<int:pk>', EliminarMiembro.as_view(), name='miembros-eliminar'),
    path('prestamos/', PrestamoList.as_view(), name='prestamos-list'),
    path('prestamos/crear/', CrearPrestamo.as_view(), name='prestamos-crear'),
    path('prestamos/actualizar/<int:pk>', ActualizarPrestamo.as_view(), name='prestamos-actualizar'),
    path('prestamos/eliminar/<int:pk>', EliminarPrestamo.as_view(), name='prestamos-eliminar'),
    #Filtros
    path('libros/buscar-por-autor/<int:autor_id>/', LibroByAutor.as_view(), name='libros-buscar-por-autor'),
    path('libros/buscar-por-editorial/<int:editorial_id>/', LibroByEditorial.as_view(), name='libros-buscar-por-editorial'),
    path('prestamos/buscar-por-fecha/<str:fecha>/', PrestamoByFecha.as_view(), name='prestamos-buscar-por-fecha'),
    path('prestamos/buscar-por-miembro/<int:miembro_id>/', PrestamoByMiembro.as_view(), name='prestamos-buscar-por-miembro'),
    path('libros/buscar-no-devueltos/<str:fecha_inicio>/<str:fecha_fin>/', LibroByNoDevueltoRango.as_view(), name='libros-buscar-no-devueltos'),
]

