from django.shortcuts import render

from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .services import EmployeeService


class EmployeeViewSet(viewsets.ViewSet):

    def list(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        EmployeeService.validate_business_rules(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=201)

    def update(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=204)


# Create your views here.
