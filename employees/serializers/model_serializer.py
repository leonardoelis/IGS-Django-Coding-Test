from rest_framework import serializers
from ..models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']


class EmployeeQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id']
        extra_kwargs = {
            'id': {
                'read_only': False
            }
        }


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class DepartmentQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id']
        extra_kwargs = {
            'id': {
                'read_only': False
            }
        }
