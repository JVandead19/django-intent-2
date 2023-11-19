from django.db import models
# Importando el modelo User de la BD estandar de Django
from django.contrib.auth.models import User

# Create your models here.

class docent(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    name =  models.CharField(max_length=60,null=True)
    


class Estudiante(models.Model):
    userr = models.ForeignKey(User, on_delete = models.CASCADE)
    dni =  models.CharField(max_length=60,primary_key=True)
    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    edad = models.CharField(max_length=2, blank=True, null=True)
    telefono = models.CharField(max_length=11, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    fecha_de_nac  = models.CharField(max_length=10,null = True, blank = True)
    año_cursante = models.CharField(max_length=100, blank=True)
    promedio = models.CharField(max_length=5,blank=True)
    observacion = models.TextField(blank=True)
    
    def __str__(self):
        return self.dni +' - '+ self.año_cursante +' - '+ self.userr.username

class AoEscolar(models.Model):
    codigo = models.CharField(primary_key=True, max_length=15)
    año_escolar = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.año_escolar

class Asignaturas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    materia = models.CharField(max_length=100, )
    c_año_escolar = models.ForeignKey(AoEscolar, on_delete = models.CASCADE)

    def __str__(self):
        return self.codigo +' - '+ self.materia

class EAoEsc(models.Model):
    userr = models.ForeignKey(User, on_delete = models.CASCADE,null=True) 
    c_año_escolar = models.ForeignKey(AoEscolar, on_delete = models.CASCADE)
    
    

class PrimerLapso(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    dni =models.ForeignKey(Estudiante, on_delete = models.CASCADE,null=True) 
    codigo_año = models.ForeignKey(AoEscolar,on_delete = models.CASCADE)  # Field name made lowercase.
    codigo_asig = models.ForeignKey(Asignaturas,on_delete = models.CASCADE)
    materia = models.CharField(max_length=100)
    definitiva = models.CharField(max_length=2, blank=True)
    
    def __str__(self):
        return self.dni.dni +' - '+ self.materia

class SegundoLapso(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    dni = models.ForeignKey(Estudiante, on_delete = models.CASCADE) 
    codigo_año = models.ForeignKey(AoEscolar,on_delete = models.CASCADE)  # Field name made lowercase.
    codigo_asig = models.ForeignKey(Asignaturas,on_delete = models.CASCADE)
    materia = models.CharField(max_length=100)
    definitiva = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return self.dni.dni +' - '+ self.materia

class TercerLapso(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    dni = models.ForeignKey(Estudiante, on_delete = models.CASCADE) 
    codigo_año = models.ForeignKey(AoEscolar,on_delete = models.CASCADE)  # Field name made lowercase.
    codigo_asig = models.ForeignKey(Asignaturas,on_delete = models.CASCADE)
    materia = models.CharField(max_length=100)
    definitiva = models.CharField(max_length=2, blank=True)
    
    def __str__(self):
        return self.dni.dni +' - '+ self.materia
    



        
        
class Materias_año(models.Model):
    codigo_año = models.ForeignKey(AoEscolar,on_delete = models.CASCADE)
    año = models.CharField(max_length=100)
    codigo_asig = models.ForeignKey(Asignaturas,on_delete = models.CASCADE)
    materia = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
  

    def __str__(self):
        return self.año +' - '+ self.materia

class Contenido_materia(models.Model):
    titulo = models.CharField(max_length = 100,null=True)
    id_materia = models.ForeignKey(Materias_año,on_delete=models.CASCADE,null=True)
    descripcion = models.TextField(blank = True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE,null=True)
    archivos = models.FileField(upload_to="media",null=True)
    
    
    
