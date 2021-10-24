from django.shortcuts import render
from django import forms

# Create your views here.

tasks = ["Check Email", "Make Files", "Run As Administartor"]


def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })


def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add Task")
