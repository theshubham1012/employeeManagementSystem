from django.contrib import admin
from .models import Employee, Client, Site, Designation, Salary

class SalaryAdmin(admin.ModelAdmin):
    readonly_fields = [
        'calculatedBasic',
        'calculatedHRA',
        'calculatedAllowance',
        'calculatedPF',
        'calculatedESI',
        'netPay',
    ]
    fields = [
        'employeeID',
        'attendance',
        'monthDays',
        'calculatedBasic',
        'calculatedHRA',
        'calculatedAllowance',
        'calculatedPF',
        'calculatedESI',
        'netPay',
    ]
    list_display = [
        'employeeID',
        'monthDays',
        'calculatedBasic',
        'calculatedHRA',
        'calculatedAllowance',
        'calculatedPF',
        'calculatedESI',
        'netPay',
    ]

# Register your models here.
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Site)
admin.site.register(Designation)
admin.site.register(Salary, SalaryAdmin)
