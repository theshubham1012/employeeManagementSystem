from django.db import models

# Create your models here.
class Employee(models.Model):
    employeeID = models.CharField(max_length=20, unique=True, primary_key=True)
    employeeName = models.CharField(max_length=25,null=False)
    aadhar = models.CharField(max_length=12, null=False)
    mobileNum = models.CharField(max_length=10, null=False)
    account = models.CharField(max_length=50,null=False)
    accountIFSC = models.CharField(max_length=50,null=False)
    accountName = models.CharField(max_length=50,null=False)
    siteName = models.ForeignKey("Site", on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey("Designation", on_delete=models.SET_NULL, null=True)
    pan = models.CharField(max_length=15, null=True)
    uan = models.CharField(max_length=30, null=True)
    esi = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.employeeName+" "+self.employeeID

class Client(models.Model):
    clientName = models.CharField(max_length=30)
    clientAddress = models.CharField(max_length=50)
    clientGstin = models.CharField(max_length=20)

    def __str__(self):
        return self.clientName

class Site(models.Model):
    clientName = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sites")
    siteName = models.CharField(max_length=30)

    def __str__(self):
        return self.siteName

class Designation(models.Model):
    designation = models.CharField(max_length=20)
    monthlyBasic = models.FloatField(default=0.0)
    monthlyHRA = models.FloatField(default=0.0)
    monthlyAllowance = models.FloatField(default=0.0)

    
    def __str__(self):
        return self.designation


class Salary(models.Model):
    employeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.IntegerField()
    claculatedBasic = models.FloatField(editable=False, default=0.0)
    calculatedHRA = models.FloatField(editable=False, default=0.0)
    calculatedAllowance = models.FloatField(editable=False, default=0.0)
    calculatedPF = models.FloatField(editable=False, default=0.0)
    calculatedESI = models.FloatField(editable=False, default=0.0)
    netPay = models.FloatField(editable=False, default=0.0)
    monthDays = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        employee = self.employeeID  # actual Employee instance
        designation = employee.designation
        monthlyBasic = designation.monthlyBasic
        monthlyHRA = designation.monthlyHRA
        monthlyAllowance = designation.monthlyAllowance

        self.claculatedBasic = (monthlyBasic / 26) * self.attendance
        self.calculatedHRA = (monthlyHRA / 26) * self.attendance
        self.calculatedAllowance = (monthlyAllowance / 26) * self.attendance
        self.calculatedPF = monthlyBasic * 12 / 100
        self.calculatedESI = monthlyBasic * 9 / 100

        # PF/ESI as deductions — flip the sign here if you actually want them added
        self.netPay = (
            self.claculatedBasic + self.calculatedHRA + self.calculatedAllowance
            - self.calculatedPF - self.calculatedESI
        )

        super().save(*args, **kwargs)