from django.db import models

# Create your models here.
class Basic(models.Model):
    # name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=20)
    electricity=models.CharField(max_length=20,primary_key=True)
    hno=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    mandal=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    # about=models.CharField(max_length=300)
    def __str__(self):
        return self.electricity

class Family(models.Model):
    name=models.CharField(max_length=100)
    electricity=models.CharField(max_length=20)
    role=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    qual=models.CharField(max_length=30)
    occupation=models.CharField(max_length=100)


    class Meta:
        unique_together = (('name', 'electricity','age'),)
    def __str__(self):
        return self.name
