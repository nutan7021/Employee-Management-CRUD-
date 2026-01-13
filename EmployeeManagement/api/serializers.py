from rest_framework import serializers
from api.models import Employee, Department, Attendance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_id', 'name', 'location']

class EmployeeSerializer(serializers.ModelSerializer):

    # department = DepartmentSerializer(read_only=True)
    def validate_salary(self, value):
        if value <= 0:
            raise serializers.ValidationError("Salary must be greater than 0")
        return value

    # def validate_email(self, value):
    #     if not value.endswith("@example.com"):
    #         raise 
            
    #         serializers.ValidationError("Email is not valid")
    #     return value
            
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'email', 'department', 'salary']


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Attendance.objects.all(),
                fields=["employee", "date"],
                message="Attendance already marked for this date."
            )
        ]
