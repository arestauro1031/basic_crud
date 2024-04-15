from django.db import models

# Create your models here.

class Position(models.Model):
    
    positionID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)


class Employee(models.Model):
    
    empID = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    
    mobileno = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    