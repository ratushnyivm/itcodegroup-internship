from django.views import generic

from .models import Material


class MaterialListView(generic.ListView):
    """Generic class-based view for a list of materials."""

    model = Material
    template_name = 'materials/material_list.html'
    context_object_name = 'materials'


class MaterialDetailView(generic.DetailView):
    """Generic class-based view for detail displaying a material."""

    model = Material
    template_name = 'materials/material_detail.html'
