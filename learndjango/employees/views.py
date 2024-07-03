from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Employee
from .forms import EmployeeForm

from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Employee
from .forms import EmployeeForm
from .serializers import EmployeeSerializer

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
            return redirect('employees')
    else:
        form = EmployeeForm()
    
    return render(request, 'employee_add.html', {'form': form})