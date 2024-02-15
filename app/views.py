from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from django.conf import settings
# Create your views here.

def home(request):
    publicidadListados = Publicidad.objects.all()
    programaListados = Programa.objects.all()
    subProgramaListados = Programacion.objects.all()
    nutricania = Cania.objects.all()
    #return render(request, 'home.html')
    return render(request,"home.html",{"publicidad": publicidadListados,"programa": programaListados,"Programacion":subProgramaListados,"nutri":nutricania})

def artistas(request):
    artistasListados = Artista.objects.all()
    #return render(request, 'artistas.html')
    return render(request,"artistas.html",{"artistas": artistasListados})

def contacto(request):
    return render(request, 'contacto.html')


def registrar_contacto(request):
    nombre = request.POST['name']
    correo = request.POST['email']
    numero = request.POST['phone']
    mensaje = request.POST['message']

    contacto = Contacto.objects.create(nombre=nombre,correo=correo,numero=numero,mensaje=mensaje)

    return redirect('/contacto')

def television(request):
    return render(request, 'rstv.html')

def hilos(request):
    usuarioHilo = UsuariosHilo.objects.all()
    return render(request,"hilos/hilos.html", {"usuario": usuarioHilo})

# #####################################################################################################################

# # def login_admin(request):
# #     if request.method == 'GET':
# #         return render(request,"registration/login.html",{'form':AuthenticationForm})
# #     else:
# #         name = request.POST["username"]
# #         password = request.POST["password"]
# #         user = authenticate(username=name,password=password)
# #         if user is None:
# #             return render(request,"registration/login.html",{'form':AuthenticationForm,'error':"Usuario y/o contraseña incorrectos"})
# #         else:
# #             login(request, user)
# #             return redirect("/administracion")

# # @login_required
# # def administracion(request):
# #     return render(request, 'views_admin/administracion.html')

# # ----------------- CRUD PROGRAMAS ------------------------------------

# # Metodo 1
# def admin_Programas(request):
#     programaListados = Programa.objects.all()

#     if request.method == 'POST':
#         form = ProgramaForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminProgramas")
#     else:
#         programaForm = ProgramaForm()
#     return render(request,'views_admin/crud_programas/adminProgramas.html',{'form':programaForm, 'programa': programaListados})

# # Metodo 2 (Context) 
# def editar_Programa(request,id):
#     programa = Programa.objects.get(id=id)
#     form = ProgramaForm(instance=programa)
#     context = {'form':form}
#     if request.method == 'POST':
#         form = ProgramaForm(request.POST, request.FILES, instance=programa)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminProgramas")
#     else:
#         programaForm = ProgramaForm()
#     return render(request,'views_admin/crud_programas/editarProgramas.html',context)

# def eliminar_programa(request, id):
#     programa = Programa.objects.get(id=id)
#     programa.delete()

#     return redirect("/adminProgramas")

# # ----------------- CRUD PROGRAMACION ------------------------------------

# def admin_Programacion(request):
#     programacionListados = Programacion.objects.all()

#     if request.method == 'POST':
#         form = ProgramacionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminProgramacion")
#     else:
#         programacionForm = ProgramacionForm()
#     return render(request,'views_admin/crud_programacion/adminProgramacion.html',{'form':programacionForm, 'programacion': programacionListados})

# def editar_Programacion(request,id):
#     programacion = Programacion.objects.get(id=id)
#     form = ProgramacionForm(instance=programacion)
#     context = {'form':form}
#     if request.method == 'POST':
#         form = ProgramacionForm(request.POST, request.FILES, instance=programacion)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminProgramacion")
#     else:
#         programaForm = ProgramaForm()
#     return render(request,'views_admin/crud_programacion/editarProgramacion.html',context)

# def eliminar_programacion(request, id):
#     programacion = Programacion.objects.get(id=id)
#     programacion.delete()

#     return redirect("/adminProgramacion")

# # ----------------- CRUD ARTISTAS ------------------------------------

# def admin_artistas(request):
#     artistaListados = Artista.objects.all()

#     if request.method == 'POST':
#         form = ArtistaForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminArtistas")
#     else:
#         artistaForm = ArtistaForm()
#     return render(request,'views_admin/crud_artistas/adminArtistas.html',{'form':artistaForm, 'artista': artistaListados})

# def editar_Artista(request,id):
#     artista = Artista.objects.get(id=id)
#     form = ArtistaForm(instance=artista)
#     context = {'form':form}
#     if request.method == 'POST':
#         form = ArtistaForm(request.POST, request.FILES, instance=artista)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminArtistas")
#     else:
#         programaForm = ProgramaForm()
#     return render(request,'views_admin/crud_artistas/editarArtistas.html',context)

# def eliminar_artista(request, id):
#     artista = Artista.objects.get(id=id)
#     artista.delete()

#     return redirect("/adminArtistas")

# # ----------------- CRUD PUBLICIDAD ------------------------------------

# def admin_publicidad(request):
#     publicidadListados = Publicidad.objects.all()

#     if request.method == 'POST':
#         form = PublicidadForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminPublicidad")
#     else:
#         publicidadForm = PublicidadForm()
#     return render(request,'views_admin/crud_publicidad/adminPublicidad.html',{'form':publicidadForm, 'publicidad': publicidadListados})

# def editar_publicidad(request,id):
#     publicidad = Publicidad.objects.get(id=id)
#     form = PublicidadForm(instance=publicidad)
#     context = {'form':form}
#     if request.method == 'POST':
#         form = ArtistaForm(request.POST, request.FILES, instance=publicidad)
#         if form.is_valid():
#             form.save()
#             return redirect("/adminPublicidad")
#     else:
#         publicidadForm = PublicidadForm()
#     return render(request,'views_admin/crud_publicidad/editarPublicidad.html',context)

# def eliminar_publicidad(request, id):
#     publicidad = Publicidad.objects.get(id=id)
#     publicidad.delete()

#     return redirect("/adminPublicidad")

# # ----------------- CONSULTA CONTACTO ------------------------------------

# def admin_contacto(request):
#     contactoListados = Contacto.objects.all()

#     return render(request,'views_admin/views_contacto/adminContacto.html',{'contacto': contactoListados})

# def eliminar_contacto(request, id):
#     contacto = Contacto.objects.get(id=id)
#     contacto.delete()

#     return redirect("/adminContacto")