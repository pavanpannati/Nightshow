# Generated by Django 5.1.1 on 2024-09-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_movie_posters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_posters',
            name='movie',
            field=models.ImageField(upload_to='images/'),
        ),
    ]