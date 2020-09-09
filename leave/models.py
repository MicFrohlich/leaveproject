from django.db import models
from phone_field import PhoneField


class Employee(models.Model):
    emp_number = models.CharField(max_length=20, blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)


class EmployeeLeave(models.Model):
    leave_statuses = [
        ("New", "N"),
        ("Approved", "A"),
        ("Declined", "D"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    days_of_leave = models.IntegerField(blank=True)
    status = models.CharField(max_length=15, choices=leave_statuses)
