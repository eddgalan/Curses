from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4, null=True)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title