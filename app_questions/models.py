from django.db import models

# Create your models here.

class AskedQuestions(models.Model):
    question = models.CharField(max_length=450)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'asked_questions'
