from django.db.models import Count, Sum
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from division.models import Departament
from division.serializer import DepartamentSerializer


class DepartamentViewSet(viewsets.ModelViewSet):
    """ API для получения списка депортаментов (включая искуственное поле
     с числом сотрудников + поле с суммарным окладам по всем сотрудникам"""

    serializer_class = DepartamentSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        qs = Departament.objects.annotate(
            all_employee=Count('employees'),
            all_salary=Sum('employees__salary')
        )
        return qs
