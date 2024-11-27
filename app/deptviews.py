from django.shortcuts import render,redirect
from .forms import departmentDetails
from .models import Employee, Department
from django.contrib import messages
from django.urls import reverse



# Department Details
def dept_details(request):
    if request.method == 'GET':
        return render(request,'detailsform/deptdetails.html',{'dept_form':departmentDetails})
    elif request.method == 'POST':
        dept_id = request.POST.get('dept_id')
        dept_name = request.POST.get('dept_name')
        mng_id = int(request.POST.get('manager_id'))
        dept_location = request.POST.get('dept_location')

        manager = []
        for managerID in Employee.objects.all():
            manager.append(managerID.manager_id)
        print(len(manager),mng_id,type(mng_id),manager)
        if len(manager)>0 and mng_id not in manager:
            messages.error(request,'Manager ID not matched')
        else:
            Department.objects.create(
                dept_id = dept_id,
                dept_name = dept_name,
                manager_id = mng_id,
                dept_location = dept_location,
            )
            messages.success(request,'Department Added')
        return render(request,'detailsform/deptdetails.html',{'dept_form':departmentDetails,'status':'department details inserted'})

# Department Manage
def dept_manage(request):
    dept = [values for values in Department.objects.all()]
    print(dept,11111111111)
    return render(request,'manageform/deptmanage.html',{'dept_manage':dept})

# Department Edit
def dept_edit(request,dept_id):
    if request.method == 'GET':
        deptID = Department.objects.get(dept_id=dept_id)
        return render(request,'detailsform/deptdetails.html',{'dept_form':departmentDetails(instance=deptID)})
    elif request.method == 'POST':
        dept_id = request.POST.get('dept_id')
        dept_name = request.POST.get('dept_name')
        manager_id = request.POST.get('manager_id')
        location = request.POST.get('dept_location')

        # To save in DB
        department = Department.objects.get(dept_id = dept_id)

        department.dept_id = dept_id
        department.dept_name = dept_name
        department.manager_id = manager_id
        department.dept_location = location

        department.save()
        messages.success(request,f'{dept_id} edited successfully')

        return redirect(reverse('deptmanage'))
    return render(request,'manageform/deptmanage.html')
        
# To delete Department
def dept_delete(request,dept_id):
    if request.method == 'GET':
        deptID = Department.objects.get(dept_id = dept_id)
        deptID.delete()
        messages.success(request,f'{dept_id} deleted')
        return redirect(reverse('deptmanage'))
    return render(request,'manageform/deptmanage.html')
