from django.contrib import admin
from .models import Usuario, Bloque, Semana, Dia, Ejercicio

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Bloque)
admin.site.register(Semana)
admin.site.register(Dia)
admin.site.register(Ejercicio)