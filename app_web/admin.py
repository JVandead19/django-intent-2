from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Importando los modelos que se encuentran en el modulo 'models.py'
from .models import Estudiante,AoEscolar,Asignaturas,EAoEsc,PrimerLapso,SegundoLapso,TercerLapso,Materias_año,Contenido_materia,docent

# Agregamos los modelos importados o class creadas al panel admin
admin.site.register(Estudiante)
admin.site.register(AoEscolar)
admin.site.register(Asignaturas)
admin.site.register(EAoEsc)
admin.site.register(PrimerLapso)
admin.site.register(SegundoLapso)
admin.site.register(TercerLapso)
admin.site.register(Materias_año)
admin.site.register(Contenido_materia)
admin.site.register(docent)