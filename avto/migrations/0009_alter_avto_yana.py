# Generated by Django 5.0.1 on 2024-01-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0008_alter_avto_dvigatel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avto',
            name='yana',
            field=models.TextField(blank=True, null=True, verbose_name='qushimcha'),
        ),
    ]