# Generated by Django 5.0.1 on 2024-01-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avto', '0004_alter_avto_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='avto',
            name='dvigatel',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dvigatel Hajmi'),
        ),
        migrations.AddField(
            model_name='avto',
            name='savdolashuv',
            field=models.CharField(blank=True, choices=[('Savdolashuv bor', 'Savdolashuv bor')], max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='avto',
            name='xolati',
            field=models.CharField(blank=True, choices=[('Avtosalon', 'Avtosalon')], max_length=99, null=True),
        ),
    ]
