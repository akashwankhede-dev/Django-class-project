from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='productImages/')

    def __str__(self):
        return self.name