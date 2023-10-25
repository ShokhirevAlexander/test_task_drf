from django.urls import path, include
from rest_framework.routers import SimpleRouter

from division.views import DepartamentViewSet


routers = SimpleRouter()
routers.register('departament', DepartamentViewSet, 'departament')

urlpatterns = [
    path('', include(routers.urls)),
]