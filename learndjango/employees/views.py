from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Employee
from .forms import EmployeeForm

from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Employee
from .forms import EmployeeForm

def employees(request):
    myemployees = Employee.objects.all()
    return render(request, 'employees_list.html', {'myemployees': myemployees})

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'myemployee'

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')  # Redirect to the employees view
    else:
        form = EmployeeForm()
    
    return render(request, 'employee_add.html', {'form': form})

# def employees(request):
#     myemployees = Employee.objects.all().values()
#     template = loader.get_template('employees_list.html')
#     context = {
#         'myemployees': myemployees,
#     }
#     return HttpResponse(template.render(context, request))

# def details(request, id):
#     myemployee = Employee.objects.get(id=id)
#     template = loader.get_template('employee_detail.html')
#     context = {
#         'myemployee': myemployee,
#     }
#     return HttpResponse(template.render(context, request))

# def add_employee(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('employees_list')  # Replace with the name of the view to display the employee list
#     else:
#         form = EmployeeForm()
    
#     return render(request, 'employee_add.html', {'form': form})