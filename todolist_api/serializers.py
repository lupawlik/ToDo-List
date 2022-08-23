from rest_framework import serializers
from employees_main.models import Task, Employee


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(source="filtered_task_items", many=True, read_only=True)

    class Meta:
        model = Employee
        fields = (
            "id",
            "name",
            "surname",
            "tasks",
        )
