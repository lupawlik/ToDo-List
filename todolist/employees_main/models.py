from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Task(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'Aktywne', _('Active')
        CLOSED = 'Zamkniete', _('Closed')

    status = models.CharField(max_length=9, choices=Status.choices)
    category = models.CharField(max_length=30)
    deadline_date = models.DateField()
    description = models.TextField(null=True, blank=True, help_text="Add description")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name="tasks")

    def get_status(self):
        return self.Status[self.status]