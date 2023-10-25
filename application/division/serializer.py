from rest_framework import serializers

from division.models import Departament


class DepartamentSerializer(serializers.ModelSerializer):
    all_employee = serializers.IntegerField()
    all_salary = serializers.FloatField()

    class Meta:
        model = Departament
        fields = ('title', 'all_employee', 'all_salary')
