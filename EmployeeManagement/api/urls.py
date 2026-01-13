from django.urls import path
from .views import EmployeeViewSet, DepartmentViewSet
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProfileView, CheckInView, CheckOutView


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

department_list = DepartmentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

department_detail = DepartmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('employees/', employee_list),
    path('employees/<int:pk>/', employee_detail),

    path('departments/', department_list),
    path('departments/<int:pk>/', department_detail),
    path("profile/", ProfileView.as_view()),
    path("attendance/check_in/", CheckInView.as_view()),
    path("attendance/check_out/", CheckOutView.as_view()),
]
