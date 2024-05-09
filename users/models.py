
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class MyUserManager(UserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        user = User.objects.create(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='имя')
    position = models.CharField(max_length=150, verbose_name='должность')
    is_staff = models.BooleanField(default=False, verbose_name="статус staff")
    is_active = models.BooleanField(
        default=True, verbose_name="статус активности"
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




