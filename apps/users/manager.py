from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager,models.Manager):
    def _create_user(self,username, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, True, **extra_fields)

    def create_superuser(self, username, password=None,is_active=True, **extra_fields):
        return self._create_user(username, password, True, True, is_active, **extra_fields)