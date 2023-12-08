from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)

    def _str_(self):
        return self.dname
    
class Emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def _str_(self):
        return self.ename