from django.test import TestCase
from django.urls import reverse

from .models import Client, Designation, Employee, Salary, Site


class AttendanceUpdateTests(TestCase):
    def setUp(self):
        client = Client.objects.create(
            clientName='Test Client',
            clientAddress='Test Address',
            clientGstin='29ABCDE1234F1Z5',
        )
        site = Site.objects.create(clientName=client, siteName='Test Site')
        designation = Designation.objects.create(
            designation='Engineer',
            monthlyBasic=1000,
            monthlyHRA=200,
            monthlyAllowance=100,
        )
        self.employee = Employee.objects.create(
            employeeID='EMP001',
            employeeName='John Doe',
            aadhar='123456789012',
            mobileNum='9876543210',
            account='1234567890',
            accountIFSC='SBIN0001234',
            accountName='John Doe',
            siteName=site,
            designation=designation,
            pan='ABCDE1234F',
            uan='123456789012',
            esi='1234567890',
        )
        self.salary = Salary.objects.create(employeeID=self.employee, attendance=10)

    def test_attendance_update_recalculates_salary_fields(self):
        initial_total = self.salary.totalA

        response = self.client.post(
            reverse('mark-attendance'),
            {f'attendance_{self.employee.pk}': 20},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.salary.refresh_from_db()
        self.assertEqual(self.salary.attendance, 20)
        self.assertNotEqual(self.salary.totalA, initial_total)
