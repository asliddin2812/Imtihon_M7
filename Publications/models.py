from django.db import models
from packaging.tags import Tag


# Create your models here.
class Publications(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='media/publication/images/', default='media/publication/images/default.jpg')
    tags = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '-' + self.tags

    class Meta:
        ordering = ['-created_at']
        db_table = 'publications'
