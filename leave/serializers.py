from rest_framework import serializers

from leave.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "emp_number",
            "phone_number",
            "first_name",
            "last_name",
        ]