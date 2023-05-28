from django.shortcuts import redirect, render
from .form import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'employee_register/employee_list.html', context)


def employee_form(request):

    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'employee_register/employee_form.html', context)

def employee_update(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'employee_register/employee_form.html', context)

def employee_delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/')
