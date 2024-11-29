from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def view_indexEmployees(request):
    employees=Employee.objects.all()
    return render(request,"employees.html",{"employees1":employees})

def registerEmployee(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    dir=request.POST["txtdir"]

    saveEmployee=Employee.objects.create(employee_id=id,employee_name=name,employee_dir=dir)#GUARDA EL REGISTRO

    return redirect("Employees")

def selectEmployee(request,employee_id):
    employees=Employee.objects.get(employee_id=employee_id)
    return render(request,"editE.html",{"employees1":employees})

def editEmployee(request):
    id=request.POST["txtid"]
    name=request.POST["txtname"]
    dir=request.POST["txtdir"]
    employees=Employee.objects.get(employee_id=id)
    employees.employee_name=name
    employees.employee_dir=dir
    
    employees.save() # actualiza registros
    return redirect("Employees")

def deleteEmployee(request,employee_id):
    employees=Employee.objects.get(employee_id=employee_id)
    employees.delete() # borra el registro

    return redirect("Employees")
