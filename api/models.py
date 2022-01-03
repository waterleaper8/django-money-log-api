from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Universal Unique ID
import uuid
from datetime import date
from django.utils import timezone

# ユーザーネーム認証をメールアドレス認証に書き換える
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is must')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4,
                        primary_key=True, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Bill(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                        primary_key=True, editable=False)
    create_user = models.ForeignKey(to=get_user_model(),on_delete=models.DO_NOTHING, default=get_user_model())
    created_at = models.DateTimeField(default=timezone.now)
    isCalc = models.BooleanField(default=True)
    date = models.DateField(blank=False, default=date.today)
    title = models.CharField(max_length=30, default="", blank=True)
    amount = models.IntegerField(blank=False)
    pocket = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=30, default="未分類", blank=True)
    subcategory = models.CharField(max_length=30, default='未分類', blank=True)
    memo = models.CharField(max_length=30, default="", blank=True)

    def __str__(self):
        return self.title

class Pocket(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                        primary_key=True, editable=False)
    create_user = models.ForeignKey(to=get_user_model(),on_delete=models.DO_NOTHING, default=get_user_model())
    category = models.CharField(max_length=30, blank=False)
    name = models.CharField(max_length=30, blank=False)
    amount = models.IntegerField(blank=False)
