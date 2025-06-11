from django.db import models

from Publications.models import Publications
# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=70)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)
    public_id = models.ForeignKey(Publications, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.author

    class Meta:
        ordering = ['-created']
        db_table = 'paper'