# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Project
from apps.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    This is User model that can be admin or just user of certain center.
    We give permissions leave the Users status (ex: Admin, User of Center...)
    Every User's username have to unique.
    Every User privileges begin as default User, not stuff, admin, superuser
    """
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    username = models.CharField(max_length=255, unique=True)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    def is_member(self, *groups):
        """
        This method used to check group of user.
        If result will be True then User member of this group otherwise not member
        :return: boolean
        """
        return self.groups.filter(name__in=groups).exists()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
