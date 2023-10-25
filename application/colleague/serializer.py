from rest_framework import routers, serializers, viewsets

from colleague.models import Employee
from division.models import Departament


class EmployeeSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField()

    class Meta:
        model = Employee
        fields = ('surname', 'name', 'patronymic', 'post', 'salary', 'age', 'department_name')

    def create(self, validated_data):
        departament_title = validated_data.pop('departament')['title']
        departament = Departament.objects.get(title=departament_title)
        employee = Employee.objects.create(departament=departament, **validated_data)
        return employee
