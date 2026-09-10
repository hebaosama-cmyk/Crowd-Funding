from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    mobile_number = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        null=True,
        blank=True
    )

    birthdate = models.DateField(
        null=True,
        blank=True
    )

    facebook_profile = models.URLField(
        max_length=200,
        null=True,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )