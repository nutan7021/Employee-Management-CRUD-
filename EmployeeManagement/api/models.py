from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from .validators import company_email_validator
from django.contrib.auth.models import User

class Department(models.Model):
    department_id = models.CharField(max_length= 50, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.department_id} - {self.name}"

class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee",
        null=True,
        blank=True
    )
    employee_id = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators = [company_email_validator])
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name="employees"
    )
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

# Create your models here.

class Attendance(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="attendance_records"
    )
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ("PRESENT", "Present"),
            ("ABSENT", "Absent"),
            ("LEAVE", "Leave")
        ]
    )

    class Meta:
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee.employee_id} - {self.date}"


