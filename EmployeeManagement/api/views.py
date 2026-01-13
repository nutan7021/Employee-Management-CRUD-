from django.shortcuts import render

from rest_framework import viewsets
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .services import EmployeeService
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView

from datetime import date, datetime
from .models import Attendance
from rest_framework import status

class EmployeeViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]

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
class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]




# this is for to get know wether the login user is admin or employee
# so we directly sedning as an json to the frontend
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            "username": user.username,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
        })


# For marking the check in date and timing in the attendance table
class CheckInView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            employee = request.user.employee
        except Employee.DoesNotExist:
            return Response(
                {"detail": "Employee profile not found for this user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        today = date.today()

        attendance, created = Attendance.objects.get_or_create(
            employee=employee,
            date=today,
            defaults={
                "check_in": datetime.now().time(),
                "status": "PRESENT"
            }
        )
        print(created)

        if not created:
            return Response(
                {"detail": "You have already checked in today"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {"detail": "Check-in successful"},
            status=status.HTTP_201_CREATED
        )


class CheckOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee = request.user.employee
        today = date.today()

        try:
            attendance = Attendance.objects.get(
                employee=employee,
                date=today
            )
        except Attendance.DoesNotExist:
            return Response(
                {"detail": "Check-in not found for today"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if attendance.check_out:
            return Response(
                {"detail": "You have already checked out"},
                status=status.HTTP_400_BAD_REQUEST
            )

        attendance.check_out = datetime.now().time()
        attendance.save()

        return Response(
            {"detail": "Check-out successful"},
            status=status.HTTP_200_OK
        )
