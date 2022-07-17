from drf_yasg import openapi
from ..serializers.model_serializer import EmployeeSerializer, DepartmentSerializer


get_employee_response = {
    "200": openapi.Response('Successful operation', EmployeeSerializer)
}

post_employee_response = {
    "201": openapi.Response('Employee created', EmployeeSerializer),
    "400": openapi.Response('Bad Request - Invalid input')
}

delete_employee_response = {
    "204": openapi.Response('Employee deleted'),
    "404": openapi.Response('Employee not found')
}


get_department_response = {
    "200": openapi.Response('Successful operation', DepartmentSerializer)
}

post_department_response = {
    "201": openapi.Response('Department created', DepartmentSerializer),
    "400": openapi.Response('Bad Request - Invalid input')
}

delete_department_response = {
    "204": openapi.Response('Department deleted'),
    "404": openapi.Response('Department not found')
}