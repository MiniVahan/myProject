from django.db import models


class Student(models.Model):
    name = models.TextField()
    surname = models.TextField()
    age = models.TextField()

    def __str__(self):
        return self.name


