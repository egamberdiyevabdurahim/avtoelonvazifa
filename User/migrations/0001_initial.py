# Generated by Django 5.0.1 on 2024-01-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=20, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=20, verbose_name='Familiya')),
                ('password', models.CharField(max_length=20, verbose_name='Parol')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefon Numer')),
                ('photo', models.ImageField(upload_to='user_photo/', verbose_name='Rasm')),
            ],
        ),
    ]