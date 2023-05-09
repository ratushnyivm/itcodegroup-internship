from django.urls import path

from .views import PartDetailView, PartListView

app_name = 'parts'

urlpatterns = [
    path('', PartListView.as_view(), name='part_list'),
    path('<int:pk>/', PartDetailView.as_view(), name='part_detail'),
]
