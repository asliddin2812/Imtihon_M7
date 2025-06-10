from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserProfile(AbstractUser):
    job_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/profile/images/', default='media/profile/images/default.jpg')
    is_user = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 'UserProfile'