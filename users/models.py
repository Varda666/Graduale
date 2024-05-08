
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class MyUserManager(UserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        user = User.objects.create(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    # USER_ROLE_CHOISES = [
    #     ('issue_executor', 'issue_executor'),
    #     ('owner', 'owner')
    # ]
    username = None
    first_name = None
    last_name = None
    # user_role = models.CharField(
    #     choices=USER_ROLE_CHOISES,
    #     verbose_name='роль'
    # )
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='имя')
    # position = models.CharField(max_length=150, verbose_name='должность')
    is_staff = models.BooleanField(default=False, verbose_name="статус staff")
    is_active = models.BooleanField(
        default=True, verbose_name="статус активности"
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




