# Generated by Django 5.1.1 on 2024-09-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_remove_register_password1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=90),
        ),
    ]