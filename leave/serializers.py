from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator, UniqueForYearValidator

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
    start_date = serializers.DateTimeField(format="%Y-%m-%d")
    end_date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = EmployeeLeave
        fields = ["employee", "start_date", "end_date", "status"]
        read_only_fields = ["days_of_leave"]
        validators = [
            UniqueTogetherValidator(
                queryset=EmployeeLeave.objects.all(), fields=["employee", "start_date"]
            ),
            UniqueTogetherValidator(
                queryset=EmployeeLeave.objects.all(), fields=["employee", "end_date"]
            )
        ]

    def validate(self, data):
        """Assert that End date not before start date"""
        if data["end_date"].day < data["start_date"].day:
            raise serializers.ValidationError(
                {"end_date": "cannot have end date before start date"}
            )
        if data["end_date"].month < data["start_date"].month:
            raise serializers.ValidationError(
                {"end_date": "cannot have end date before start date"}
            )
        if data["end_date"].year < data["start_date"].year:
            raise serializers.ValidationError(
                {"end_date": "cannot have end date before start date"}
            )
        if data["start_date"].day == data["end_date"].day:
            if data["end_date"].hour < data["start_date"].hour:
                raise serializers.ValidationError(
                    {"end_date": "cannot have end date before start date"}
                )
            else:
                if data["end_date"].minute < data["start_date"].minute:
                    raise serializers.ValidationError(
                        {"end_date": "cannot have end date before start date"}
                    )
                else:
                    if data["end_date"].second < data["start_date"].second:
                        raise serializers.ValidationError(
                            {"end_date": "cannot have end date before start date"}
                        )
                    elif data["end_date"].second == data["start_date"].second:
                        raise serializers.ValidationError(
                            {"start_date": "cannot log leave with no leave"}
                        )
        return data

    def is_valid(self, raise_exception=False):

        # Checks for duplicated datetimes
        dts_set = set()
        for item in self.initial_data:
            if item in dts_set:
                raise ValidationError(detail="start_datetime must be unique.")
        super().is_valid(raise_exception)
