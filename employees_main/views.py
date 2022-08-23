from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Employee, Task
from .forms import AddNewEmployee, AddNewTask

import csv
import unidecode


# returns all tasks for a current employee id
def export_csv(request, id_e):
    try:
        emp = Employee.objects.get(id=id_e)
        tasks = emp.tasks.all()
    except ObjectDoesNotExist:
        return redirect("/")

    name = unidecode.unidecode(str(emp)).replace(" ", "_")

    response = HttpResponse("")
    response['Content-Disposition'] = f'attachment; filename="{name}_tasks.csv"'

    writer = csv.writer(response)
    writer.writerow(['Status', 'Kategoria', 'Deadline', 'Opis'])
    fields = tasks.values_list('status', 'category', 'deadline_date', 'description')

    for row in fields:
        writer.writerow(row)
    return response

# main page with all employees
def index(request):
    all_employees = Employee.objects.all()
    form = AddNewEmployee()
    return render(request, "employees_main/index.html", {"all_employees": all_employees, "form": form})

# adds new employee to db
def add_new_e(request):
    if request.method == "POST":
        form = AddNewEmployee(request.POST)
        if form.is_valid():
            e = Employee(name=form.cleaned_data["name"], surname=form.cleaned_data["surname"])
            e.save()
        return redirect("/")

    return redirect("/")

def employee(request, id_e):
    try:
        emp = Employee.objects.get(id=id_e)
        tasks = emp.tasks.all()
        form = AddNewTask()
    except ObjectDoesNotExist:
        return redirect("/")

    if request.method == "POST":
        form = AddNewTask(request.POST)
        if form.is_valid():
            t = Task(status=form.cleaned_data["status"],
                     category=form.cleaned_data["category"],
                     deadline_date=form.cleaned_data["deadline_date"],
                     description=form.cleaned_data["description"],
                     employee=emp)
            t.save()
            return redirect(f"/employee/{id_e}")
    return render(request, "employees_main/employee.html", {"employee": emp, "tasks": tasks, "form": form})

def update_task(resposne, id_t):
    if resposne.method == "POST":
        action = resposne.POST["action"]
        if action == "change_status":
            new_status = resposne.POST["new_status"]
            Task.objects.filter(id=id_t).update(status=new_status)
        elif action == "remove":
            Task.objects.filter(id=id_t).delete()

        return HttpResponse('')
