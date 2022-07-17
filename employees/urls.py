from django.urls import path
from .api.views import EmployeeView, DepartmentView
from .views import listAllEmployees

urlpatterns = [
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('department/', DepartmentView.as_view(), name='department'),
    path('employee/list', listAllEmployees, name='listAllEmployees')
]