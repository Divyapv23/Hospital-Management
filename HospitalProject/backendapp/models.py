from django.db import models

# Create your models here.

class adminlogin(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)


class departmentdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Description = models.CharField(max_length=1000, null=True, blank=True)

class doctordb(models.Model):
    Drname=models.CharField(max_length=100,null=True,blank=True)
    Dept=models.CharField(max_length=100,null=True,blank=True)
    Drimage=models.ImageField(upload_to="profile",null=True,blank=True)
    Qul=models.CharField(max_length=100,null=True,blank=True)
