from django.contrib import admin

from .models import Assembly, AssemblyPart


class AssemblyPartInline(admin.TabularInline):
    model = AssemblyPart
    autocomplete_fields = ('part',)
    extra = 10


@admin.register(Assembly)
class AssemblyAdmin(admin.ModelAdmin):
    list_display = ('designation', 'name', 'created', 'updated')
    inlines = [AssemblyPartInline]


@admin.register(AssemblyPart)
class AssemblyPartAdmin(admin.ModelAdmin):
    list_display = ('assembly', 'part', 'part_count')
