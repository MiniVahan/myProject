from django.db import models


class Question(models.Model):
    question = models.TextField()
    answer1 = models.CharField(max_length=20)
    answer2 = models.CharField(max_length=20)
    answer3 = models.CharField(max_length=20)
    answer4 = models.CharField(max_length=20)
    right_answer = models.CharField(max_length=20)

    def __str__(self):
        return self.question[:50]


# Create your models here.
