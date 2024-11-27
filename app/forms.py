from django import forms
from .models import Signup, Employee, Department, Client, Project

# signup details form
class signupPage(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Signup
        fields = '__all__'

# Employee details form
class employeeDetails(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

manager = [(value,value) for value in Employee.objects.values_list('manager_id',flat=True)]
# Department details form
class departmentDetails(forms.ModelForm):
    manager_id = forms.ChoiceField(
        choices=manager,
        label='Select manager',
        required=False,
    )
    class Meta:
        model = Department
        fields = '__all__'

# Client Details
class clientDetails(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'