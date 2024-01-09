from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name="Username")
    first_name = models.CharField(max_length=20, verbose_name="Ism")
    last_name = models.CharField(max_length=20, verbose_name="Familiya")
    password = models.CharField(max_length=20, verbose_name="Parol")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Telefon Numer")
    photo = models.ImageField(upload_to='user_photo/', verbose_name="Rasm")

    def __str__(self):
        return self.username

# class AuthUser(AbstractUser):
#     STATUS = [
#         ('Admin', 'ADMIN'),
#         ('Adminstrator', 'ADMINSTRATOR'),
#         ('User', 'User'),
#     ]
#     status = models.CharField(max_length=9909, choices=STATUS, default='user')
#
#     photo = models.ImageField(upload_to='user_photo', null=True, blank=True)
#     phone = models.CharField(max_length=13)