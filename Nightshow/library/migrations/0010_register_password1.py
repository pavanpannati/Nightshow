# Generated by Django 5.1.1 on 2024-09-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_remove_register_password1_remove_register_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]