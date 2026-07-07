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
    employeeID = models.OneToOneField(Employee, on_delete=models.CASCADE)
    attendance = models.IntegerField()
    monthDays = models.IntegerField(default=30)
    claculatedBasic = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    calculatedHRA = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    calculatedAllowance = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    totalA = models.IntegerField(default=0)
    calculatedPF = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    calculatedESI = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    deductions = models.IntegerField(default=0)
    netPay = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        employee = self.employeeID  # actual Employee instance
        designation = employee.designation
        monthlyBasic = designation.monthlyBasic
        monthlyHRA = designation.monthlyHRA
        monthlyAllowance = designation.monthlyAllowance

        self.claculatedBasic = (monthlyBasic / 26) * self.attendance
        self.calculatedHRA = (monthlyHRA / 26) * self.attendance
        self.calculatedAllowance = (monthlyAllowance / 26) * self.attendance
        self.totalA = self.claculatedBasic + self.calculatedHRA + self.calculatedAllowance
        self.calculatedPF = self.claculatedBasic * 12 / 100
        self.calculatedESI = self.claculatedBasic * 9 / 100
        self.deductions = self.calculatedPF + self.calculatedESI
        # PF/ESI as deductions — flip the sign here if you actually want them added
        self.netPay = (
            self.totalA - self.deductions
        )

        super().save(*args, **kwargs)