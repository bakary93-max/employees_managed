from django.db import models


# Create your models here.


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        template = '{0.id} {0.name} {0.salary}'
        return template.format(self)
    