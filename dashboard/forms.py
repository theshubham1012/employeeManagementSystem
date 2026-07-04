from django import forms
from .models import Employee, Salary, Client, Site, Designation

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class SiteForm(forms.ModelForm):
    class Meta:
        model=Site
        fields = '__all__'

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'

class BulkAttendanceForm(forms.Form):
    def __init__(self, *args, employees=None, **kwargs):
        super().__init__(*args, **kwargs)
        if employees is None:
            employees = Employee.objects.all()

        for employee in employees:
            salary_record = Salary.objects.filter(employeeID=employee).last()
            initial_value = salary_record.attendance if salary_record else 0
            self.fields[f'attendance_{employee.pk}'] = forms.IntegerField(
                label=f"{employee.employeeName} ({employee.employeeID})",
                required=False,
                min_value=0,
                max_value=31,
                initial=initial_value,
            )