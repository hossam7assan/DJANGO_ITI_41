from django.shortcuts import render
from django.http import HttpResponse
from products.models import Department
# Create your views here.

def index(request):
    # call landing page in dir home/index.html
    # list all Departments
    depatments = Department.objects.filter(active=1)
    return render(request, 'home/index.html', {'all_departments' : depatments})

