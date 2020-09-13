from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from leave.models import Employee, EmployeeLeave
from leave.serializers import EmployeeSerializer, EmployeeLeaveSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated, )


class EmployeeLeaveViewSet(viewsets.ModelViewSet):
    queryset = EmployeeLeave.objects.all()
    serializer_class = EmployeeLeaveSerializer
    permission_classes = (IsAuthenticated, )
