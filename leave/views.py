from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from leave.models import Employee
from leave.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer