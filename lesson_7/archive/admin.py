from django.contrib import admin

from .models import Assembly, AssemblyPart, Material, Part


class AssemblyPartInline(admin.TabularInline):
    model = AssemblyPart
    autocomplete_fields = ('part',)
    extra = 10


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name', 'created')


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('designation', 'name', 'material', 'created', 'updated')
    search_fields = ('designation', 'name')
    autocomplete_fields = ('material',)


@admin.register(Assembly)
class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('designation', 'name', 'created', 'updated')
    inlines = [AssemblyPartInline]
