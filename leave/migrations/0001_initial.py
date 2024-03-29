# Generated by Django 3.1.1 on 2020-09-09 17:56

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("emp_number", models.CharField(blank=True, max_length=20)),
                (
                    "phone_number",
                    phone_field.models.PhoneField(
                        blank=True, help_text="Contact phone number", max_length=31
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=50)),
                ("last_name", models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeLeave",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateTimeField(blank=True)),
                ("end_date", models.DateTimeField(blank=True)),
                ("days_of_leave", models.IntegerField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("New", "N"), ("Approved", "A"), ("Declined", "D")],
                        max_length=15,
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="leave.employee"
                    ),
                ),
            ],
        ),
    ]
