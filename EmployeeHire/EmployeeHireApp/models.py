from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField()

    def hiredyear(self):
        return self.hire_date.strftime('%Y')
    class Meta:
        db_table = 'employees'


class Department(models.Model):
    dept_no = models.CharField(primary_key=True,max_length=4)
    dept_name = models.CharField(max_length=40,unique=True)

    class Meta:
        db_table = 'departments'

class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee,on_delete=models.CASCADE,db_column='emp_no')
    dept_no = models.ForeignKey(Department,on_delete=models.CASCADE,db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_emp'

class Title(models.Model):
    emp_no = models.ForeignKey(Employee,on_delete=models.CASCADE,db_column='emp_no')
    title = models.CharField(primary_key=True,max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'titles'

class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no')
    salary = models.IntegerField()
    from_date = models.DateField(unique=True)
    to_date = models.DateField()

    class Meta:
        db_table = 'salaries'







