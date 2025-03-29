from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    OCCUPATION_CHOICES = [
        ('law student', "LAW STUDENT"),
        ('lawyer', "LAWYER"),
        ('bar candidate', "BAR CANDIDATE"),
    ]

    email = models.EmailField(_("email address"), unique=True)
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True, unique=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
