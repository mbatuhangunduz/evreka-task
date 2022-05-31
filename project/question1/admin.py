from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import NavigationRecord, Vehicle
from import_export.admin import ImportExportActionModelAdmin

@admin.register(NavigationRecord)
class NavigationRecord(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("datetime","vehicle",)
    list_filter = ("vehicle",)
    group_fieldsets = True


@admin.register(Vehicle)
class Vehicle(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("plate",)
    list_filter = ("plate",)
    group_fieldsets = True