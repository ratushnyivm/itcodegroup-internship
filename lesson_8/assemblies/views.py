from django.views import generic

from .models import Assembly


class AssemblyListView(generic.ListView):
    """Generic class-based view for a list of assemblies."""

    model = Assembly
    template_name = 'assemblies/assembly_list.html'
    context_object_name = 'assemblies'


class AssemblyDetailView(generic.DetailView):
    """Generic class-based view for detail displaying an assembly."""

    model = Assembly
    template_name = 'assemblies/assembly_detail.html'
