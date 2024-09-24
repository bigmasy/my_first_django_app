from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Customer_user(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Унікальне ім'я
        blank=True,
        help_text=("The groups this user belongs to."),
        verbose_name=("groups"),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Унікальне ім'я
        blank=True,
        help_text=("Specific permissions for this user."),
        verbose_name=("user permissions"),
    )
