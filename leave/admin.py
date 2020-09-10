from django.contrib import admin

# Register your models here.
from leave.models import Employee, EmployeeLeave

admin.site.register(Employee)
admin.site.register(EmployeeLeave)
