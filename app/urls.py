from django.contrib import admin
from django.urls import path
from django import views
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name="home"),
    path('artistas/', views.artistas, name='artistas'),
    path('contacto/', views.contacto, name='contacto'),
    path('television/', views.television, name='television'),
    path('registrarContacto/', views.registrar_contacto, name='registrarContacto'),
    path('hilos/', views.hilos, name="Hilos"),
    # path('login/', views.login_admin, name='login'),
    # path('administracion/', views.administracion, name='administracion'),
    # path('adminProgramas/', views.admin_Programas, name='adminProgramas'),
    # path('eliminarPrograma/<int:id>/', views.eliminar_programa , name='eliminacionPrograma'),
    # path('editarPrograma/<int:id>/', views.editar_Programa, name='editarPrograma'),
    # path('adminArtistas/', views.admin_artistas, name='adminArtistas'),
    # path('editarArtista/<int:id>/', views.editar_Artista, name='editarArtista'),
    # path('eliminarArtista/<int:id>/', views.eliminar_artista , name='eliminacionArtista'),
    # path('adminProgramacion/', views.admin_Programacion, name='adminProgramacion'),
    # path('eliminarProgramacion/<int:id>/', views.eliminar_programacion, name='eliminarProgramacion'),
    # path('editarProgramacion/<int:id>/', views.editar_Programacion, name='editarProgramacion'),
    # path('adminPublicidad/', views.admin_publicidad, name='adminPublicidad'),
    # path('editarPublicidad/<int:id>/', views.editar_publicidad, name='editarPublicidad'),
    # path('eliminarPublicidad/<int:id>/', views.eliminar_publicidad, name='eliminarPublicidad'),
    # path('adminContacto/', views.admin_contacto, name='adminContacto'),
    # path('eliminarContacto/<int:id>/', views.eliminar_contacto, name='eliminarContacto'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # to import static in deployment

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)