# api/services.py
from rest_framework.exceptions import ValidationError

class EmployeeService:

    @staticmethod
    def validate_business_rules(data):
        department = data.get("department")
        salary = data.get("salary")

        if department == "Product" and salary < 1500000:
            raise ValidationError(
                "For Product department, salary must be greater than 15L"
            )

        return data
