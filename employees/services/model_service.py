from django.http import Http404

from ..models import Employee, Department
from ..serializers.model_serializer import EmployeeSerializer, DepartmentSerializer


class EmployeeService:

    def findAll(self):
        return Employee.objects.all()

    def save(self, request_body):
        employee_serializer = EmployeeSerializer(data=request_body)
        if employee_serializer.is_valid(raise_exception=True):
            employee = employee_serializer.save()
            return employee

    def delete(self, id):
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
        except Employee.DoesNotExist:
            raise Http404()


class DepartmentService:

    def findAll(self):
        return Department.objects.all()

    def save(self, request_body):
        department_serializer = DepartmentSerializer(data=request_body)
        if department_serializer.is_valid(raise_exception=True):
            department = department_serializer.save()
            return department

    def delete(self, id):
        try:
            department = Department.objects.get(id=id)
            department.delete()
        except Department.DoesNotExist:
            raise Http404()

