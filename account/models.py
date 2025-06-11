import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('User', _('User')),
        ('reviewer', _('Reviewer')),
        ('SuperAdmin', _('SuperAdmin')),
    )
    role = models.CharField(max_length=30, choices=USER_ROLES, verbose_name=_('Role'))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('Birth Date'))
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    organization = models.CharField(max_length=300, blank=True, verbose_name=_('Organization'))
    image = models.ImageField(upload_to='media/profile/images/', blank=True, null=True, verbose_name=_('Image'))
    position = models.CharField(max_length=300, blank=True, null=True, verbose_name=_('Position'))

    def __str__(self):
        return f"{self.username} - {self.role}"

    def save(self, *args, **kwargs):
        if self.role == 'SuperAdmin' and not self.pk:
            if CustomUser.objects.filter(role='SuperAdmin').count() >= 4:
                raise ValueError(_("SuperAdminlar soni 4 tadan oshmasligi kerak."))
        super().save(*args, **kwargs)

    @classmethod
    def create_user(cls, **kwargs):
        password = kwargs.pop('password', None)
        user = cls(**kwargs)
        if password:
            user.set_password(password)
        user.save()
        return user

    class Meta:
        db_table = 'CustomUser'


class PasswordResetCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('User'))
    code = models.UUIDField(default=uuid.uuid4, unique=True, verbose_name=_('Code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    expires_at = models.DateTimeField(verbose_name=_('Expires At'))

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(minutes=30)
        super().save(*args, **kwargs)

    def is_valid(self):
        return timezone.now() <= self.expires_at

    class Meta:
        db_table = 'PasswordResetCode'