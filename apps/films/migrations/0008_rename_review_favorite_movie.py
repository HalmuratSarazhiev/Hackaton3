# Generated by Django 4.0.5 on 2022-07-05 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_rename_image_movie_poster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='review',
            new_name='movie',
        ),
    ]