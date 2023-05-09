from django.urls import path

from .views import MaterialDetailView, MaterialListView

app_name = 'materials'

urlpatterns = [
    path('', MaterialListView.as_view(), name='material_list'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='material_detail'),
]
