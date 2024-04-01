from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        location=int(request.POST['location'])
        dept=request.POST['dept']
        role=request.POST['role']
        new_emp=Employee(first_name=firstname,last_name=lastname,sal=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added Successfully')
    elif request.method=="GET":
        return render(request,'add_emp.html')
    else:
        return HttpResponse('An Exception Occured! Employee Cannot Be Added')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_remove=Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("Employee Remove Successfully")
        except:
            return HttpResponse("Please Enter A Valid Email Id")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)


def filter_emp(request):
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        salary=request.POST['salary']
        dept=request.POST['dept']
        role=request.POST['role']
        bonus=request.POST['bonus']
        emps=Employee.objects.all()
        if firstname:
            emps=emps.filter(first_name__contains=firstname)
        if lastname:
            emps=emps.filter(lastname__contains=lastname)
        if salary:
            emps=emps.filter(sal__contains=salary)
        if dept:
            emps=emps.filter(dept__name__contains=dept)
        if role:
            emps=emps.filter(role__contains=role)
        if bonus:
            emps=emps.filter(bonus__contains=bonus)
        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("invalid")
