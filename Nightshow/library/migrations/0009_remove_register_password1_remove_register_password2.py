# Generated by Django 5.1.1 on 2024-09-29 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_register_options_alter_register_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password2',
        ),
    ]