from django.contrib import admin
from .models import Empleados,Productos,Ventas,Compras,Infoventas
# Register your models here.

admin.site.register(Empleados)
admin.site.register(Productos)
admin.site.register(Ventas)
admin.site.register(Compras)
admin.site.register(Infoventas)
