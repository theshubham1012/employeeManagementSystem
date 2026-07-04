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

def addSite(request):
    if request.method=='POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addSite')
    form = SiteForm()
    return render(request, 'add-site.html',{'form':form,})

def addDesignation(request):
    if request.method=='POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addDesignation')

    form = DesignationForm()
    return render(request, 'add-designation.html', {'form':form})

#---------------------------------------#####  Attendance related views   #####--------------------------------------#
def markAttendance(request):
    employees = Employee.objects.all()

    if request.method == 'POST':
        form = BulkAttendanceForm(request.POST, employees=employees)
        if form.is_valid():
            for employee in employees:
                field_name = f'attendance_{employee.pk}'
                attendance_value = form.cleaned_data.get(field_name, 0)
                Salary.objects.update_or_create(
                    employeeID=employee,
                    defaults={'attendance': attendance_value},
                )
            return redirect('home')
    else:
        form = BulkAttendanceForm(employees=employees)

    return render(request, 'mark_attendance.html', {'form': form})


#---------------------------------------##### Data/Sheets related views   #####--------------------------------------#

def allEmployees(request):
    employees = Employee.objects.all()
    return render(request, 'sheets/all_employees.html',{'employees':employees})