from django.contrib import admin

from .models import Employe


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "poste", "salaire")
    search_fields = ("name", "email", "poste")
