from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='productImages/')

    def __str__(self):
        return self.name

class MyCourse(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    