from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=60)
    contraseña = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.nombre_usuario}: {self.contraseña}"

class Bloque(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Bloque'
        verbose_name_plural = 'Bloques'

    def __str__(self):
        return f"{self.usuario}: {self.nombre}"
    
class Semana(models.Model):
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)
    numero = models.IntegerField()

    class Meta:
        verbose_name = 'Semana'
        verbose_name_plural = 'Semanas'

    def __str__(self):
        return f"{self.numero}"
    
class Dia(models.Model):
    semana = models.ForeignKey(Semana, on_delete=models.CASCADE)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)
    nombre_dia = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Dia'
        verbose_name_plural = 'Dias'

    def __str__(self):
        return f"{self.semana.numero}: {self.nombre_dia}"
    
class Ejercicio(models.Model):
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    peso = models.IntegerField()
    repeticiones = models.IntegerField()
    observaciones = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return f"{self.nombre}"