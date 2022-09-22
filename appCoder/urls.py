from django.urls import path
from appCoder.views import *

urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('home/', home),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiante/', buscar_estudiante),
    path('create_estudiantes/', create_estudiantes),
    path('read_estudiantes/', read_estudiantes),
    path('update_estudiantes/<estudiante_id>', update_estudiantes),
    path('delete_estudiantes/<estudiante_id>', delete_estudiantes),
    path('curso/list',CursoList.as_view(),name="List"),
    path(r'^(?P<pk>\d+)$',CursoDetalle.as_view(), name="Detail"),
    path(r'^nuevo$',CursoCreacion.as_view(),name="New"),
    path(r'^editar/(?P<pk>\d+)$',CursoUpdate.as_view(),name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$',CursoDelete.as_view(),name="Delete"),
]