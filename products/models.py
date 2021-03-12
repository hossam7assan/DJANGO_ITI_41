from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # photo = models.ImageField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # visible = models.BooleanField(default=False)

