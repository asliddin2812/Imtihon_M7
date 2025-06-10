from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=130)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=13,unique=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name + ' ' + self.mobile_number

    class Meta:
        db_table = 'contacts'
        ordering = ['-created_at']
        