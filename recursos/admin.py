from django.contrib import admin
from recursos.models import *

class InsumoRecursoInline(admin.StackedInline):
  model = InsumoRecurso
  extra = 1

class VersionRecursoInline(admin.StackedInline):
  model = VersionRecurso
  extra = 1

class RecursoAdmin(admin.ModelAdmin):
  inlines = [InsumoRecursoInline, VersionRecursoInline]

# Register your models here.
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(InsumoRecurso)
admin.site.register(VersionRecurso)
admin.site.register(Tag)
admin.site.register(FechaEntrega)
admin.site.register(ComentarioRecurso)
