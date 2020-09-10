from rest_framework import serializers

from leave.models import Employee, EmployeeLeave


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "emp_number",
            "phone_number",
            "first_name",
            "last_name",
        ]


class EmployeeLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLeave
        fields = [
            "employee",
            "start_date",
            "end_date",
            "days_of_leave",
            "status"
        ]