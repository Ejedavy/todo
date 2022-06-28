import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, telegram_link, telegram_userID, nickname, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not telegram_link:
            raise ValueError(_("You must provide the telegram link"))
        if not telegram_userID:
            raise ValueError(_("You must provide the telegram user ID"))
        if not nickname:
            raise ValueError(_("You must provide the nickname"))

        email = self.normalize_email(email)
        user = self.model(email=email, telegram_link=telegram_link,
                          telegram_userID=telegram_userID, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, telegram_link, telegram_userID, nickname, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault("firstname", "David")
        extra_fields.setdefault("lastname", "Eje")

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email=email, telegram_link=telegram_link, telegram_userID=telegram_userID,
                                nickname=nickname, password=password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    telegram_link = models.URLField(blank=False, null=False)
    telegram_userID = models.IntegerField(blank=False)
    email = models.EmailField(_("email address"), unique=True)
    nickname = models.CharField(max_length=50, unique=True, blank=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    genderChoices = [("Male", "Male"), ("Female", "Female"), ("Rather not say", "Rather not say")]
    gender = models.CharField(choices=genderChoices, max_length=150, null=False, blank=False, default="Rather not say")
    is_active = models.BooleanField(default=False)
    image = models.FileField(upload_to="profilePictures", default=None)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['telegram_link', 'telegram_userID', 'nickname']
    objects = CustomUserManager()
