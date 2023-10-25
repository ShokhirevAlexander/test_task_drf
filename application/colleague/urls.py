from django.urls import path, include
from rest_framework.routers import SimpleRouter

from colleague.views import EmployeeViewSet


routers = SimpleRouter()
routers.register('employee', EmployeeViewSet, 'employee')

urlpatterns = [
    path('', include(routers.urls)),
]
