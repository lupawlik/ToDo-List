from django.shortcuts import render
import datetime

from django.db.models import Prefetch
from employees_main.models import Task, Employee
from rest_framework import generics
from .serializers import EmployeeSerializer
# Create your views here.

class EmployeeListView(generics.ListCreateAPIView):
    http_method_names = ['get']
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        cur_date = datetime.datetime.now().strftime("%Y-%m-%d")
        queryset = Employee.objects.prefetch_related(
            Prefetch("tasks", to_attr="filtered_task_items", queryset=Task.objects.filter(deadline_date=cur_date))).filter(tasks__deadline_date=cur_date)
        return queryset

