from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from datetime import datetime
from .models import Autor, Editorial, Libro, Miembro, Prestamo
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer, PrestamoSerializer


# ====================== VISTAS DE LIBROS ======================

# Listar autores
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def get(self, request):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        if not autores:
            raise NotFound('No se encontraron autores.')
        return Response(
            {
                'success': True,
                'detail': 'Listado de autores.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Crear autores
class CrearAutor(generics.CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Autor creado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

# Actualizar autores
class ActualizarAutor(generics.UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def put(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)

        serializer = AutorSerializer(autor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'success': True,
                'detail': 'Autor actualizada correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )
    
# Eliminar Autor
class EliminarAutor(generics.DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def delete(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        autor.delete()
        return Response(
            {
                'success': True,
                'detail': 'Autor eliminado correctamente.'
            },
            status=status.HTTP_204_NO_CONTENT
        )

# ====================== VISTAS DE EDITORIAL ======================
# Listar editoriales
class EditorialList(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def get(self, request):
        editoriales = Editorial.objects.all()
        serializer = EditorialSerializer(editoriales, many=True)
        if not editoriales:
            raise NotFound('No se encontraron editoriales.')
        return Response(
            {
                'success': True,
                'detail': 'Listado de editoriales.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Crear editorial
class CrearEditorial(generics.CreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def post(self, request):
        serializer = EditorialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Editorial creado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

# Actualizar editorial
class ActualizarEditorial(generics.UpdateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def put(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)

        serializer = EditorialSerializer(editorial, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Editorial actualizado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Eliminar editorial
class EliminarEditorial(generics.DestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def delete(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)
        editorial.delete()
        return Response(
            {
                'success': True,
                'detail': 'Editorial eliminado correctamente.'
            },
            status=status.HTTP_204_NO_CONTENT
        )


# ====================== VISTAS DE LIBROS ======================
# Listar libros
class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        if not libros:
            raise NotFound('No se encontraron libros.')
        return Response(
            {
                'success': True,
                'detail': 'Listado de libros.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Crear libros
class CrearLibro(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Libro creado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

# Actualizar libros
class ActualizarLibro(generics.UpdateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def put(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)

        serializer = LibroSerializer(libro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Libro actualizado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Eliminar libros    
class EliminarLibro(generics.DestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def delete(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.delete()
        return Response(
            {
                'success': True,
                'detail': 'Libro eliminado correctamente.'
            },
            status=status.HTTP_204_NO_CONTENT
        )

# ====================== VISTAS DE MIEMBRRO ======================
# Listar miembros
class MiembroList(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get(self, request):
        miembros = Miembro.objects.all()
        serializer = MiembroSerializer(miembros, many=True)
        if not miembros:
            raise NotFound('No se encontraron miembros.')
        return Response(
            {
                'success': True,
                'detail': 'Listado de miembros.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Crear miembros
class CrearMiembro(generics.CreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def post(self, request):
        serializer = MiembroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Miembro creado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

# Actualizar miembros
class ActualizarMiembro(generics.UpdateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def put(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        email = request.data.get('email', None)

        # Verificar si el email ha cambiado
        if email and email != miembro.email:
            # Verificar si ya existe otro miembro con el mismo email
            if Miembro.objects.filter(email=email).exclude(pk=pk).exists():
                return Response(
                    {'email': ['Miembro con este email ya existe.']},
                    status=status.HTTP_400_BAD_REQUEST
                )

        serializer = MiembroSerializer(miembro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Miembro actualizado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Eliminar miembros
class EliminarMiembro(generics.DestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def delete(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        miembro.delete()
        return Response(
            {
                'success': True,
                'detail': 'Miembro eliminado correctamente.'
            },
            status=status.HTTP_204_NO_CONTENT
        )

# ====================== VISTAS DE PRESTAMO ======================
# Listar prestamos
class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request):
        prestamos = Prestamo.objects.all()
        serializer = PrestamoSerializer(prestamos, many=True)
        if not prestamos:
            raise NotFound('No se encontraron prestamos.')
        return Response(
            {
                'success': True,
                'detail': 'Listado de prestamos.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )   

# Crear prestamos
class CrearPrestamo(generics.CreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def post(self, request):
        serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Prestamo creado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

# Actualizar prestamos
class ActualizarPrestamo(generics.UpdateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def put(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)

        serializer = PrestamoSerializer(prestamo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'success': True,
                'detail': 'Prestamo actualizado correctamente.',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )

# Eliminar prestamos
class EliminarPrestamo(generics.DestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def delete(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        prestamo.delete()
        return Response(
            {
                'success': True,
                'detail': 'Prestamo eliminado correctamente.'
            },
            status=status.HTTP_204_NO_CONTENT
        )