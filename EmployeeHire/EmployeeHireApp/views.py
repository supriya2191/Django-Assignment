from django.shortcuts import render
from .forms import EmployeeForm,DepartmentForm,DeptEmpForm,SalariesForm,TitleForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse,HttpResponse
from django.views.generic import View
from .models import Employee,Department,DeptEmp,Title
import datetime
from datetime import date
from django.core.serializers import serialize
import json

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeHireCBV(View):
    curr_age=0
    exp=0
    format = '%Y-%m-%d'
    today = date.today()
    def age(self,birth):
        b=datetime.datetime.strptime(birth, self.format)
        self.curr_age = self.today.year - b.year -((self.today.month, self.today.day) < (b.month, b.day))

    def experience(self,hire):
        h=datetime.datetime.strptime(hire, self.format)
        self.exp=self.today.year - h.year -((self.today.month, self.today.day) < (h.month, h.day))
        print(self.exp)

    def post(self, request, *args, **kwargs):
        empdata = json.loads(request.body)
        for item in empdata:
            birth = item['birth_date']
            self.age(birth)
            if self.curr_age in range(18,61):
                form = EmployeeForm(item)
                if form.is_valid():
                    form.save(commit=True)
                    continue
                else:
                    return HttpResponse("Error while inserting record")
            else:
                 print('Employee age must be between 18-60')
        return HttpResponse("Successfully Inserted all records")

    def get(self, request, emp_no, *args, **kwargs):
        try:
            emp_data = Employee.objects.get(emp_no=emp_no)
            json_data=serialize('json',[emp_data])
            pdata=json.loads(json_data)
            final_list=[]
            for item in pdata:
                edata=item['fields']
                final_list.append(edata)
            json_data=json.dumps(final_list)
            return HttpResponse(json_data,content_type='application/json',status=200)
        except Employee.DoesNotExist:
            return HttpResponse("Request id not available", status=404)















