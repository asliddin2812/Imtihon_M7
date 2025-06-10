from django.db import models

# Create your models here.
class Requirements(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'requirements'
