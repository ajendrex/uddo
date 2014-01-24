from django.contrib import admin
from recursos.models import *

# Register your models here.
admin.site.register(Recurso)
admin.site.register(InsumoRecurso)
admin.site.register(Tag)
admin.site.register(FechaEntrega)
admin.site.register(ComentarioRecurso)
