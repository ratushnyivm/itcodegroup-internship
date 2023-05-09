from django.views import generic

from .models import Part


class PartListView(generic.ListView):
    """Generic class-based view for a list of parts."""

    model = Part
    template_name = 'parts/part_list.html'
    context_object_name = 'parts'


class PartDetailView(generic.DetailView):
    """Generic class-based view for detail displaying a part."""

    model = Part
    template_name = 'parts/part_detail.html'
