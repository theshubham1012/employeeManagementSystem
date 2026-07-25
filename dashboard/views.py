from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddEmployeeForm, BulkAttendanceForm, ClientForm, SiteForm, DesignationForm
from .models import Employee, Salary, Designation, Client, Site


# Create your views here.
def home(request):
    return render(request, 'home.html')


#---------------------------------------#####  Employee related views   #####--------------------------------------#
def addEmployee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('all-employees') # redirect uses url name 'name'
    form = AddEmployeeForm()
    return render(request, 'employee_registration_form.html', {'form': form})

def editEmployee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method=='POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('all-employees')
    form = AddEmployeeForm(instance=employee)
    context = {
        'form':form,
        'employee': employee
        }
    return render(request, 'edit-employee.html',context)

def deleteEmployee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('all-employees')

#---------------------------------------#####  Client related views   #####--------------------------------------#

def addClient(request):
    if request.method=='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addClient')
    form = ClientForm()
    return render(request,'add_client.html',{'form':form})

def editClient(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method=='POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('all-clients')
    form = ClientForm(instance=client)
    context={
        'form':form,
        'client':client,
    }
    return render(request, 'edit-client.html', context)

def deleteClient(request, pk):
    client = get_object_or_404(Client, pk-pk)
    client.delete()
    return redirect('all-clients')


#---------------------------------------#####  Site related views   #####--------------------------------------#

def addSite(request):
    if request.method=='POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('all-sites')
    form = SiteForm()
    return render(request, 'add-site.html',{'form':form,})

def editSite(request, pk):
    site = get_object_or_404(Site, pk=pk)
    if request.method=='POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('all-sites')
    form = SiteForm(instance=site)
    context={
        'form':form,
        'site':site,
    }
    return render(request, 'edit-site.html', context)

def deleteSite(request, pk):
    site = get_object_or_404(Site, pk=pk)
    site.delete()
    return redirect('all-sites')

#---------------------------------------#####  Designation related views   #####--------------------------------------#

def addDesignation(request):
    if request.method=='POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addDesignation')

    form = DesignationForm()
    return render(request, 'add-designation.html', {'form':form})

def editDesignation(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    if request.method == 'POST':
        form = DesignationForm(request.POST, instance=designation)
        if form.is_valid():
            form.save()
        #return redirect('')
    form = DesignationForm(instance=designation)
    return render(request, 'edit-designation.html', {'form':form})

def deleteDesignation(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    designation.delete()


#---------------------------------------#####  Attendance related views   #####--------------------------------------#
def updateAttendance(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        form = BulkAttendanceForm(request.POST, employees=employees)
        if form.is_valid():
            for employee in employees:
                field_name = f'attendance_{employee.pk}'
                attendance_value = form.cleaned_data.get(field_name, 0) or 0
                salary_record, created = Salary.objects.get_or_create(employeeID=employee) 
                salary_record.attendance = attendance_value 
                salary_record.save()
            return redirect('all-employees-salary')
    else:
        form = BulkAttendanceForm(employees=employees)

    return render(request, 'mark_attendance.html', {'form': form})


#---------------------------------------##### Data/Sheets related views   #####--------------------------------------#

def allEmployees(request):
    employees = Employee.objects.all()
    return render(request, 'sheets/all_employees.html',{'employees':employees})

def allEmployeesSalary(request):
    employees = Employee.objects.all()
    return render(request,'sheets/salary.html',{'employees':employees})

def salarySlips(request):
    employees = Employee.objects.all()
    designations = Designation.objects.all()
    salaries = Salary.objects.all()
    context = {
        'employees':employees,
        'designations' : designations,
        'salaries' : salaries
    }
    return render(request, 'sheets/salary-slips.html',context)

def allClients(request):
    clients = Client.objects.all()
    return render(request, 'sheets/all-clients.html', {'clients':clients})

def allSites(request):
    clients = Client.objects.all().prefetch_related('sites')
    context = {
        'clients': clients,
    }
    return render(request, 'sheets/all_site.html', context)


#------------------------------ Editable Sheets ------------------------------------
def editAllEmployees(request):
    employees = Employee.objects.all()
    return render(request, 'editableSheets/all_employees.html',{'employees':employees})

def editAllClients(request):
    clients = Client.objects.all()
    return render(request, 'sheets/all-clients.html', {'clients':clients})

def editAllSites(request):
    clients = Client.objects.all().prefetch_related('sites')
    context = {
        'clients': clients,
    }
    return render(request, 'sheets/all_site.html', context)