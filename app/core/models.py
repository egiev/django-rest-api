from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """ Create and save a new user """
        if not email:
            raise ValueError('Invalid email address')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that support using email instead of username """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_action = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    """ Override username by using email """
    USERNAME_FIELD = 'email'
