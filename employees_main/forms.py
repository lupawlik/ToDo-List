from django import forms

class AddNewEmployee(forms.Form):
    name = forms.CharField(label="Imię", max_length=30)
    surname = forms.CharField(label="Nazwisko", max_length=30)

    name.widget.attrs.update({"class": "form-control", "placeholder": "Podaj imię..."})
    surname.widget.attrs.update({"class": "form-control", "placeholder": "Podaj nazwisko..."})

class DatePickerInput(forms.DateInput):
    input_type = "date"

class AddNewTask(forms.Form):
    CHOICES = (
        ("Aktywne", "Aktywne"),
        ("Zamkniete", "Zamknięte"),
    )

    status = forms.ChoiceField(label="Status", choices=CHOICES)
    category = forms.CharField(label="Kategoria", max_length=30)
    deadline_date = forms.DateField(label="Deadline", widget=DatePickerInput)
    description = forms.CharField(label="Opis", max_length=300)

    status.widget.attrs.update({"class": "form-control"})
    category.widget.attrs.update({"class": "form-control"})
    deadline_date.widget.attrs.update({"class": "form-control datetimepicker-input"})
    description.widget.attrs.update({"class": "form-control"})