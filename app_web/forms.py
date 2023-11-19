# Importamos ModelForm que nos permite crear un Form acorde a los datos que le requerimos dentro de un modelo
from django.forms import ModelForm
# Importamos el modelo Tareas
from .models import Contenido_materia

from django import forms


# Creamos un Form acorde a los datos que se requieren
class Aggconten_materia(forms.ModelForm):
    class Meta:
        model = Contenido_materia
        fields = ['titulo','descripcion','archivos']
        # # # Con widgets le agg un atributo class para el form, asi modificandolo
        # # widgets = {
        # #     'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Ingresa descripcion de tarea'})
        # }
        
