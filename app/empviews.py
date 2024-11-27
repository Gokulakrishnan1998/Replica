from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.urls import reverse

# Display List
def list(request):
    if request.method == 'GET':
        return render(request,'detailsform/displaylist.html')

#Employee details  
def emp_details(request):
    if request.method == 'GET':
        return render(request,'detailsform/empDetails.html',{'emp_form':employeeDetails})
    elif request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        emp_phone = request.POST.get('emp_phone')
        emp_role = request.POST.get('emp_role')
        manager_id = request.POST.get('manager_id')

        # department_id is Optional
        if request.POST.get('dept_id'):
            dept_id = Department.objects.get(dept_id=request.POST.get('dept_id'))
            print(dept_id)

            Employee.objects.create(
            emp_id=emp_id,
            emp_name=emp_name,
            emp_email=emp_email,
            emp_phone=emp_phone,
            emp_role=emp_role,
            dept_id=dept_id,
            manager_id=manager_id,)
        else:
            Employee.objects.create(
            emp_id=emp_id,
            emp_name=emp_name,
            emp_email=emp_email,
            emp_phone=emp_phone,
            emp_role=emp_role,
            manager_id=manager_id,)
        return render(request,'detailsform/empDetails.html',{'emp_form':employeeDetails,'status':'Employee created successfully'})
    

# To show all employee's in manage Page
def employee_manage(request):
    details = Employee.objects.all()
    emp_list=[]
    for i in details.values():
        emp_list.append(i)
    # print(emp_list)        
    return render(request,'manageform/empmanage.html',{'emp_manage':emp_list})

# To edit Employee Details
def employee_edit(request,emp_email):
    if request.method == 'GET':
        employee_email = Employee.objects.get(emp_email=emp_email)
        print(employee_email)
        return render(request,'editform/empedit.html',{'emp_edit':employeeDetails(instance=employee_email)})
    elif request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        emp_email = request.POST.get('emp_email')
        emp_phone = request.POST.get('emp_phone')
        emp_role = request.POST.get('emp_role')
        dept_id = request.POST.get('dept_id')
        manager_id = request.POST.get('manager_id')

        # To Update Employee Details
        employee = Employee.objects.get(emp_id=emp_id)#get Employee from db

        # Set the new values 
        employee.emp_name = emp_name
        employee.emp_email = emp_email
        employee.emp_phone = emp_phone
        employee.emp_role = emp_role
        employee.dept_id = Department.objects.get(dept_id=dept_id)
        employee.manager_id = manager_id

        # save the employee Details
        employee.save()
        details = Employee.objects.all()
        emp_list=[]
        for i in details.values():
            emp_list.append(i)
        return redirect(reverse('empmanage'))
    return render(request,'manageform/empmanage.html',{'emp_manage':emp_list,'status':f'{emp_email} Updated Successfully'})

# To Delete Employees

def employee_delete(request,emp_email):
        
    if request.method == 'GET':
        print(type(emp_email))
        #emp_email = request.POST.get('emp_email')
        print(emp_email,1111111111111)
        employee = Employee.objects.get(emp_email=emp_email)
        print(employee,emp_email,1111111111111)
        employee.delete()

        # To get updated DB after Delete
        details = Employee.objects.all()
        emp_list=[]
        for i in details.values():
            emp_list.append(i)
        # print(emp_list)
        # To reverse the url
        return redirect(reverse('empmanage'))
    return render(request,'manageform/empmanage.html',{'emp_manage':emp_list,'status':f'{emp_email} Deleted'})
    
    