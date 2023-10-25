from django.db.models import F
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from colleague.models import Employee
from colleague.serializer import EmployeeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EmployeeViewSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class EmployeeViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin):
    """ API для получения списка сотрудников + фильтр для поиска фамилии и
    по id департамента"""

    queryset = Employee.objects.all().select_related('departament').annotate(
        department_name=F('departament__title')
    )
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['surname', 'departament_id']
    pagination_class = EmployeeViewSetPagination
