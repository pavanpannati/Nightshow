# Generated by Django 5.1.1 on 2024-11-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_rename_video_movie_posters_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_posters',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie_posters',
            name='movie',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie_posters',
            name='posters',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
