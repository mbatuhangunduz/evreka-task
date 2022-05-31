from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Operation, Bin, BinOperation
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Operation)
class Operation(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    group_fieldsets = True


@admin.register(Bin)
class Bin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("latitude", "longitude",)
    list_filter = ("latitude", "longitude",)
    group_fieldsets = True


@admin.register(BinOperation)
class BinOperations(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ("operation","collection_frequency","last_collection",)
    list_filter = ("operation","collection_frequency","last_collection",)
    group_fieldsets = True