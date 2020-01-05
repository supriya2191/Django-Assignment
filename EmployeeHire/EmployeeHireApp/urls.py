from django.urls import path
from . import views

urlpatterns = [
    path('employee_hire/',views.EmployeeHireCBV.as_view()),
    path('emp_no/<emp_no>',views.EmployeeHireCBV.as_view()),
]