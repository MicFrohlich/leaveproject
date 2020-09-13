from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from leave.models import Employee
from leave.serializers import EmployeeSerializer
import pytest


class EmployeeTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.employee_number = "D01234"
        self.phone_number = 27844444849
        self.first_name = "Test"
        self.last_name = "User"
        self.password = "z"
        self.factory = APIRequestFactory()
        self.client = Client()

        self.test_user = Employee.objects.create(
            emp_number=self.employee_number,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
        )

    @pytest.mark.django_db
    def test_create_employee(self):
        assert isinstance(self.test_user, Employee)

    @pytest.mark.django_db
    def test_can_login(self):
        client = Client()
        request = client.post(reverse("rest_framework:login"), {'username': 'admin', 'password': 'adminadmin'})
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_employee(self):
        response = self.client.get(
            reverse("employee-list")
        )
        employees = Employee.objects.all()
        serialized_employees = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serialized_employees.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_cannot_create_employee_when_not_logged_in(self):
        response = self.client.post(
            reverse("employee-list"),
            data={
                "emp_number": "D1234",
                "phone_number": 27844444948,
                "first_name": "Mike",
                "last_name": "Test"
            },
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @pytest.mark.django_db
    def test_can_create_employee_when_logged_in(self):
        response = self.client.post(
            reverse("employee-list"),
            data={
                "emp_number": "D1234",
                "phone_number": 27844444948,
                "first_name": "Mike",
                "last_name": "Test"
            },
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
