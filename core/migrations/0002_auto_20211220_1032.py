# Generated by Django 2.2.8 on 2021-12-20 10:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
