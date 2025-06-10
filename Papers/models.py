from django.db import models

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=70)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' - ' + self.author

    class Meta:
        ordering = ['-created']
        db_table = 'paper'