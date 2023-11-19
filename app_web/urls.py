from django.urls import path,re_path
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static

# Importamos las funciones que contiene views.py
from . import views

#Rutas
urlpatterns = [
    re_path(r"^download/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path('',views.index,name = 'index'),
    path('conocenos/',views.conocenos,name = 'conocenos'),
    path('lista/',views.lista,name = 'lista'),
    path('login/',views.sign_in,name = 'sign_in'),
    path('logout/',views.desconetar,name = 'logout'),
    path('menu/',views.menu,name = 'menu'),
    path('calificaciones/',views.calificaciones,name = 'calificaciones'),
    path('mi_perfil/<int:codigo>',views.perfil,name = 'perfil'),
    path('login_docent/',views.sign_in_docent,name = 'sign_in_docent'),
    path('aula/',views.aula,name = 'aula'),
    path('aula/<int:año_esc>/año',views.aula_alumn,name = 'aulas'),
    path('aula/<int:id_materia>', views.Materia, name = 'materia'),
    path('aula/<int:id_materia>/content', views.Materia_alumn, name = 'materia_alumn'),
    path('aula/<int:id_materia>/detalles', views.detalles_tarea, name = 'detalles'),
    path('aula/<int:id_materia>/eliminar', views.eliminar, name = 'eliminar'),
    path('aula/<int:id_materia>/detalles_tarea', views.detalles_tarea_alumno, name = 'detalles_alumn'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
