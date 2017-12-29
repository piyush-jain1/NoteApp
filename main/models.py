from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=10, blank=False)

    def __unicode__(self):
        return self.phone

    # class Meta:
    #     verbose_name_plural = 'User Accounts'
    #     unique_together = ("id", "phone", "email")
