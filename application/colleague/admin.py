from django.contrib import admin
from colleague.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'salary', 'age',)
    list_filter = ('departament',)
    search_fields = ('surname', 'name', 'patronymic',)
