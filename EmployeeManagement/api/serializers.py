from rest_framework import serializers
from api.models import Employee



class EmployeeSerializer(serializers.ModelSerializer):

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
        fields = '__all__'
