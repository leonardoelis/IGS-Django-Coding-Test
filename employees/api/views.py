from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from ..services.model_service import EmployeeService, DepartmentService
from ..serializers.model_serializer import EmployeeSerializer, EmployeeQuerySerializer, DepartmentSerializer, DepartmentQuerySerializer
from ..utils.response_templates_swagger import get_employee_response, post_employee_response, delete_employee_response
from ..utils.response_templates_swagger import get_department_response, post_department_response, delete_department_response


class EmployeeView(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(responses=get_employee_response)
    def get(self, request):
        employee_service = EmployeeService()
        employees = employee_service.findAll()
        list_data = []
        for employee in employees:
            data = {}
            data['id'] = employee.id
            data['name'] = employee.name
            data['email'] = employee.email
            data['department'] = str(employee.department)
            list_data.append(data)
        print(list_data)
        return Response(list_data)

    @swagger_auto_schema(responses=post_employee_response, request_body=EmployeeSerializer)
    def post(self, request):
        request_body = request.data
        print(request_body)

        employee_service = EmployeeService()
        employee = employee_service.save(request_body)

        data = {}
        data['id'] = employee.id
        data['name'] = employee.name
        data['email'] = employee.email
        data['department'] = str(employee.department)

        return Response(data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses=delete_employee_response, query_serializer=EmployeeQuerySerializer)
    def delete(self, request):
        id = request.query_params['id']
        employee_service = EmployeeService()
        employee_service.delete(id)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentView(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(responses=get_department_response)
    def get(self, request):
        department_service = DepartmentService()
        departments = department_service.findAll()
        list_data = []
        for department in departments:
            data = {}
            data['id'] = department.id
            data['name'] = department.name
            list_data.append(data)
        print(list_data)
        return Response(list_data)

    @swagger_auto_schema(responses=post_department_response, request_body=DepartmentSerializer)
    def post(self, request):
        request_body = request.data
        print(request_body)

        department_service = DepartmentService()
        department = department_service.save(request_body)

        data = {}
        data['id'] = department.id
        data['name'] = department.name

        return Response(data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(responses=delete_department_response, query_serializer=DepartmentQuerySerializer)
    def delete(self, request):
        id = request.query_params['id']
        department_service = DepartmentService()
        department_service.delete(id)
        return Response(status=status.HTTP_204_NO_CONTENT)


