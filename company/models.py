from django.db import models

# Create your models here.
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Worker(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='workers')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.worker} - {self.date} - {'Present' if self.present else 'Absent'}"
