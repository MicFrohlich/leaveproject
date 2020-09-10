from django.test import TestCase

# Create your tests here.
from leave.models import Employee


class EmployeeTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.employee_number = "D01234"
        self.phone_number = 27844444849
        self.first_name = "Test"
        self.last_name = "User"
        self.password = "z"

        self.test_user = Employee.objects.create(
            emp_number=self.employee_number,
            phone_number=self.phone_number,
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_create_employee(self):
        assert isinstance(self.test_user, Employee)
