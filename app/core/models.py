from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class  UserMananger(BaseUserManager):
    """Helper function for creating user and super-user"""

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        if not email:
            raise ValueError('User must have an email address')
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        """Create and save a new superuser"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class  User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that use the email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserMananger()
    USERNAME_FIELD = 'email'
