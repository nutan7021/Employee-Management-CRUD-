# api/validators.py
from rest_framework import serializers

def company_email_validator(value):
    if not value.lower().endswith("@example.com"):
        raise serializers.ValidationError(
            "Email must end with @example.com"
        )
