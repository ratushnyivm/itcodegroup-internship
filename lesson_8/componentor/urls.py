from django.contrib import admin
from django.urls import include, path

from .views import index

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', index, name='home'),

    # Apps
    path('materials/', include('materials.urls', namespace='materials')),
    path('parts/', include('parts.urls', namespace='parts')),
]
