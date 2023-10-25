from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('colleagua/', include('colleague.urls')),
    path('division/', include('division.urls')),
]

urlpatterns += doc_url
