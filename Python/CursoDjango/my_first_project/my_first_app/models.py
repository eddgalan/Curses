from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4, null=True)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title