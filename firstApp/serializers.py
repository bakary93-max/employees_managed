from abc import ABC

from rest_framework import serializers

from .models import Employee

"""class EmployeeSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(primary_key=True)
    name = serializers.CharField(max_length=15)
    salary = serializers.DecimalField(max_digits=10, decimal_places=3)
    """


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary']
