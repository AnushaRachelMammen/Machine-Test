from django.db import models

# Create your models here.
class productdb(models.Model):
    Product_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Size=models.IntegerField(null=True,blank=True)
    Color=models.CharField(max_length=100,null=True,blank=True)
    Status=models.CharField(max_length=100,null=True,blank=True)

class orderdb(models.Model):
    Customer_name=models.CharField(max_length=100,null=True,blank=True)
    Pro_name=models.CharField(max_length=100,null=True,blank=True)
    Purchase_no=models.IntegerField(null=True,blank=True)