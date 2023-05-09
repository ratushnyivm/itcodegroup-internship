from django.urls import path

from .views import AssemblyDetailView, AssemblyListView

app_name = 'assemblies'

urlpatterns = [
    path('', AssemblyListView.as_view(), name='assembly_list'),
    path('<int:pk>/', AssemblyDetailView.as_view(), name='assembly_detail'),
]
