from django.shortcuts import render

from .services.model_service import EmployeeService

# Create your views here.


def listAllEmployees(request):
    employee_service = EmployeeService()
    employees = employee_service.findAll()

    context = {}
    context['employees'] = employees
    return render(request, 'employees/listAllEmployees.html', context)
