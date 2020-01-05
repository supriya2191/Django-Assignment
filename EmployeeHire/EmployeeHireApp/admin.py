from django.contrib import admin
from .models import Employee,Department,DeptEmp,Salaries,Title

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_no','birth_date','first_name','last_name','gender','hire_date']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dept_no','dept_name']

class DeptEmpAdmin(admin.ModelAdmin):
    list_display = ['emp_no','dept_no','from_date','to_date']

class SalariesAdmin(admin.ModelAdmin):
    list_display = ['emp_no','salary','from_date','to_date']

class TitleAdmin(admin.ModelAdmin):
    list_display = ['emp_no','title','from_date','to_date']


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(DeptEmp,DeptEmpAdmin)
admin.site.register(Salaries,SalariesAdmin)
admin.site.register(Title,TitleAdmin)