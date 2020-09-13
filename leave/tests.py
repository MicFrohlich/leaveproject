from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from leave.models import Employee, EmployeeLeave
from leave.serializers import EmployeeSerializer
import pytest
import datetime


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
        self.user = User.objects.create(
            username="username",
            password="TestUserPassword"
        )

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
        self.client.force_login(self.user)
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
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.django_db
    def test_can_create_employee_when_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("employee-list"),
            data={
                "emp_number": "D1234",
                "phone_number": 27844444948,
                "first_name": "Mike",
                "last_name": "Test"
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EmployeeLeaveTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.employee_number = "D01234"
        self.phone_number = 27844444849
        self.first_name = "Test"
        self.last_name = "User"
        self.password = "z"
        self.factory = APIRequestFactory()
        self.client = Client()
        self.user = User.objects.create(
            username="username",
            password="TestUserPassword"
        )

        self.test_user = Employee.objects.create(
            emp_number=self.employee_number,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name,
        )

    def test_cannot_create_leave_when_unauthed(self):
        response = self.client.post(
            reverse("leave-list"),
            data={
                "employee": 1,
                "start_date": datetime.datetime(2020, 6, 1),
                "end_date": datetime.datetime(2020, 6, 2),
                "status": EmployeeLeave.leave_statuses[0],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_get_leave_when_authed(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("leave-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_get_leave_when_not_authed(self):
        response = self.client.get(
            reverse("leave-list"),
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_post_leave_when_authed(self):
        self.client.force_login(self.user)
        start_date = datetime.datetime(2020,6,1)
        end_date = datetime.datetime(2020,6,2)
        response = self.client.post(
            reverse("leave-list"),
            data={
                "employee": self.test_user.pk,
                "start_date": start_date,
                "end_date": end_date,
                "status": "N",
            },
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
