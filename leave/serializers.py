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
        read_only_fields = ['days_of_leave']

    def validate(self, data):
        """Assert that End date not before start date"""
        if data["end_date"] < data["start_date"]:
            raise serializers.ValidationError({
                "end_date": "cannot have end date before start date"
            })
        return data
