from django.http import HttpResponse
from django.shortcuts import render
from .models import Task


# Create your views here.


def task_view(request):
    obj1 = Task.objects.all()  # //adding into database
    if request.method == 'POST':  # //fetching in form
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        obj = Task(name=name, priority=priority)
        obj.save()

    return render(request, "task_view.html", {'obj1': obj1})
