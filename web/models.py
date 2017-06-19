from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=15,unique=True,verbose_name='用户名称')
    token = models.CharField(max_length=40,db_index=True)

    def __str__(self):
        return self.username



class Works(models.Model):
    uid=models.ForeignKey('User',to_field='id')
    datetime=models.DateTimeField(null=True,blank=True)
    content=models.TextField(max_length=300,blank=True,null=True,verbose_name=' 提交故障')
