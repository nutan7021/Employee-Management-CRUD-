from django.urls import path
from .views import EmployeeViewSet

employee_list = EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('employees/', employee_list),
    path('employees/<int:pk>/', employee_detail),
]
