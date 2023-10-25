from django.contrib import admin
from division.models import Departament


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', )
