from django import forms
from .models import Employee,Department,DeptEmp,Salaries,Title

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

class DeptEmpForm(forms.ModelForm):
    class Meta:
        model=DeptEmp
        fields='__all__'

class SalariesForm(forms.ModelForm):
    class Meta:
        model=Salaries
        fields='__all__'

class TitleForm(forms.ModelForm):
    class Meta:
        model=Title
        fields='__all__'