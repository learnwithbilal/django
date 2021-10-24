from django.shortcuts import render
import datetime

# Create your views here.


now = datetime.datetime.now()

newyear = now.month == 1 and now.day == 1


def index(request):
    return render(request, "newyear/index.html", {
        "newyear": newyear
    })
