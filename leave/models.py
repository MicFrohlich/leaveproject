from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField
import datetime


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    emp_number = models.CharField(max_length=20, blank=True)
    phone_number = PhoneField(blank=True, help_text="Contact phone number")
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeLeave(models.Model):
    leave_statuses = [
        ("New", "N"),
        ("Approved", "A"),
        ("Declined", "D"),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="leave_for_employee", null=True, blank=True)
    start_date = models.DateTimeField(blank=True, default=datetime.date.today)
    end_date = models.DateTimeField(blank=True, default=datetime.date.today)
    days_of_leave = models.IntegerField(blank=True)
    status = models.CharField(max_length=15, choices=leave_statuses)

    def save(self, *args, **kwargs):
        if not self.days_of_leave:
            self.days_of_leave = self.end_date - self.start_date
            self.days_of_leave = self.days_of_leave.days
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} {self.days_of_leave} {self.start_date.day} {self.start_date.month}"
