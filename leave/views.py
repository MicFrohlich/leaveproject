from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from leave.models import Employee, EmployeeLeave
from leave.serializers import EmployeeSerializer, EmployeeLeaveSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeLeaveViewSet(viewsets.ModelViewSet):
    queryset = EmployeeLeave.objects.all()
    serializer_class = EmployeeLeaveSerializer
