# Generated by Django 5.1.1 on 2024-09-23 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='birth_year',
        ),
    ]