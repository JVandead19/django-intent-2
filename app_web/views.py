from django.http import HttpResponse, Http404
from django.conf import settings
import os
# get_object_or_404: es para enviar un mensaje de error en la pagina
# render: funciona para enviar un archivo html
# redirect: funciona para redireccionar, usando el name correspondido en la URL
from django.shortcuts import render, redirect, get_object_or_404

# Importamos login, para que este cree una cookie de usuario al iniciar sesion
# Importamos logout, eliminando la cookie de usuario, asi cerrando sesion
# Importamos authenticate, para comprobar si el usuario existe en la BD
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password 

# Importando los modelos creados
from .models import PrimerLapso,SegundoLapso,TercerLapso,EAoEsc,Estudiante,Materias_año,Contenido_materia,docent,User

from django.core.exceptions import ObjectDoesNotExist

# Importamos el Form TareaForm
from .forms import Aggconten_materia

from django.contrib.auth.decorators import login_required

# ----------------------------------------------------

def index(request):
    return render(request, 'index.html')

def lista(request):
    return render(request, 'Lista.html')

def conocenos(request):
    return render(request, 'conocenos.html')

# ---------------------------------------------------
def desconetar(request):
    logout(request)
    return redirect('index')

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            user = User.objects.get(username=username)
        except:
              return render(request, 'login.html', {
                'error': 'El usuario o contraseña es incorrecto'  
            })    
        success = check_password(password, user.password) or check_password(password.lower(), user.password)

        usern = authenticate(request,username=request.POST['username'],password=request.POST['password'])
    
        if success == False:
            return render(request, 'login.html', {
                'error': 'La contraseña es incorrecta'
            })        
        else: 
            login (request,usern)
            return redirect('menu')
           
        
    

@login_required
def menu(request):
    datos_estudiante = Estudiante.objects.filter(userr=request.user)
    materias_alumno = EAoEsc.objects.filter(userr=request.user)
    x = docent.objects.filter(user_id=request.user)
    return render(request, 'menu.html',{
        'materias_alumno': materias_alumno,
        'datos_estudiante': datos_estudiante,
        'x':x
    })
@login_required
def perfil(request,codigo):
    name_user = User.objects.filter(pk=codigo)
    datos_estudiante = Estudiante.objects.filter(userr=request.user)
    return render(request, 'usuario.html',{
        'datos_estudiante': datos_estudiante,
        'name_user': name_user,
    })
@login_required
def calificaciones(request):
    notas_1erlapso = PrimerLapso.objects.filter(user=request.user) 
    notas_2dolapso = SegundoLapso.objects.filter(user=request.user)
    notas_3erlapso = TercerLapso.objects.filter(user=request.user)
    
    return render(request, 'notas.html',{
        'notas_1erlapso': notas_1erlapso,
        'notas_2dolapso': notas_2dolapso,
        'notas_3erlapso': notas_3erlapso,
    })
@login_required
def aula_alumn(request,año_esc):
    if request.method == 'GET':
        materias = Materias_año.objects.filter( codigo_año_id = año_esc)
        return render(request, 'aula_alumn.html',{
             'materias': materias
        })     
@login_required
def Materia_alumn(request, id_materia):
    if request.method == 'GET':
        # comparamos la PK con el id_tarea para verificar si son el mismo id y mostrar informacion de este, sino mostrara un get_object_or_404
        materia = get_object_or_404(Materias_año, pk=id_materia)
        num = id_materia
        show = Contenido_materia.objects.filter(id_materia = num)
        return render(request, 'aula_materia_alumn.html', {
            'show': show
        })
@login_required
def detalles_tarea_alumno(request, id_materia):
    if request.method == 'GET':
        # comparamos la PK con el id_tarea para verificar si son el mismo id y mostrar informacion de este, sino mostrara un get_object_or_404
        x = get_object_or_404(Contenido_materia, pk=id_materia)
        a = Contenido_materia.objects.filter(pk=id_materia)
        num = id_materia
        form = Aggconten_materia(request.POST, instance=x)
        tareas = Contenido_materia.objects.filter(id = num)
        print(a)
        
        return render(request, 'conten_detail_task_materia_alumn.html', {
            'tareas': tareas,
            'form': form,
            'a':a
        })       
def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
         with open(download_path, "rb") as fh:
             response = HttpResponse(fh.read(), content_type="application/archivos")
             response["Content-Disposition"] = "inline; filename=" + os.path.basename(
                 download_path
             )
             return response      
   
# -------------------------------------------------------  
      
def sign_in_docent(request):
    if request.method == 'GET':
        return render(request, 'login_docent.html')
    else:
        userSave = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if userSave is None:
            return render(request, 'login_docent.html', {
                'error': 'El usuario o contraseña es incorrecto'
            })
        else:
            # Guardar sesion
            login (request, userSave)
            return redirect('aula')
 

@login_required           
def aula(request):
    materias = Materias_año.objects.filter( user = request.user)
    return render(request, 'aula.html',{
        'materias': materias  
    })
    

@login_required    
def Materia(request, id_materia):
    if request.method == 'GET':
        # comparamos la PK con el id_tarea para verificar si son el mismo id y mostrar informacion de este, sino mostrara un get_object_or_404
        materia = get_object_or_404(Materias_año, pk=id_materia, user=request.user)
        num = id_materia
        show = Contenido_materia.objects.filter(user=request.user, id_materia = num)
        return render(request, 'aula_materia.html', {
            'form': Aggconten_materia,
            'show': show
        })
    else:
        # Otro metodo de hacerlo, guardamos los datos que estan en el form
        try:
            form = Aggconten_materia(request.POST or None, request.FILES or None)
            new_tarea = form.save(commit=False)
            # con esto 'new_tarea.user = request.user' comprobamos a que usuario le va a pertencer la tarea, revisando la sesion en la cookie
            new_tarea.user = request.user 
            new_tarea.save()
            num = id_materia
            new_tarea.id_materia_id = num
            new_tarea.save()
            
            
            show = Contenido_materia.objects.filter(user=request.user, id_materia = num)
            return render(request, 'aula_materia.html', {
                'form': Aggconten_materia,
                'show': show
            })
        # ValueError es para manejar un error
        except ValueError:
            return render(request, 'aula_materia.html', {
                'form': Aggconten_materia,
                'error': 'Por favor, provee un dato valido'
            })          


@login_required  
def detalles_tarea(request, id_materia):
    if request.method == 'GET':
        # comparamos la PK con el id_tarea para verificar si son el mismo id y mostrar informacion de este, sino mostrara un get_object_or_404
        tareas = get_object_or_404(Contenido_materia, pk=id_materia, user=request.user)
        # En 'form = TareaForm(instance = tareas)' estamos tomando el form TareaForm y le estamos agg los datos que contiene 'tareas'
        form = Aggconten_materia(instance=tareas)
        return render(request, 'conten_detail_task_materia.html',{
            'tareas': tareas,
            'form': form       
        })
    else:
        try:
            tareas = get_object_or_404(Contenido_materia, pk=id_materia, user=request.user)
            form = Aggconten_materia(request.POST,request.FILES,instance=tareas)
            form.save()
            return redirect('aula')
        except ValueError:
            return render(request, 'conten_detail_task_materia.html', {
                'tareas': tareas,
                'form': form,
                'error': 'Error al actualizar una tarea'

            })


@login_required   
def eliminar(request, id_materia):
    tarea = get_object_or_404(Contenido_materia, pk=id_materia, user=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('aula')   
# ---------------------------------------------------------            