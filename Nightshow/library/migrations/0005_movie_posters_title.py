# Generated by Django 5.1.1 on 2024-09-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_movie_posters_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_posters',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='title'),
            preserve_default=False,
        ),
    ]
