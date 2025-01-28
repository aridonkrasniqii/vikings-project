from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vikings/', include('domain.vikings.urls')),
    path('norsemen/', include('domain.norsemen.urls')),
    path('nfl/', include('domain.nfl_team.urls')),
]
