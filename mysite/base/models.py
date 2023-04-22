from django.db import models
# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=50)
    destination = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    bus = models.ForeignKey("Bus",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Bus(models.Model):
    bus_no = models.IntegerField()
    destination = models.CharField(max_length=200)
    driver = models.CharField(max_length=50)
    source = models.CharField(max_length=200)

    def __str__(self):
        return str(self.bus_no)

