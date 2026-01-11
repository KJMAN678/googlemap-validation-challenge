from django.contrib import admin

from .models import SampleModel


@admin.register(SampleModel)
class SampleModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created_at", "updated_at")
