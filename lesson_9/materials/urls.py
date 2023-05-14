from django.urls import path

from .views import (MaterialCreateView, MaterialDeleteView, MaterialDetailView,
                    MaterialListView, MaterialUpdateView)

app_name = 'materials'

urlpatterns = [
    path('', MaterialListView.as_view(), name='material_list'),
    path('create/', MaterialCreateView.as_view(), name='material_create'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='material_detail'),
    path(
        '<int:pk>/update', MaterialUpdateView.as_view(), name='material_update'
    ),
    path(
        '<int:pk>/delete', MaterialDeleteView.as_view(), name='material_delete'
    ),
]
