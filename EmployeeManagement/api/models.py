from django.db import models
from django.db import models
from django.core.validators import MinValueValidator


class Employee(models.Model):
    employee_id = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

# Create your models here.
