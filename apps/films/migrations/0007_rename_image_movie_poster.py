# Generated by Django 4.0.5 on 2022-07-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_movie_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image',
            new_name='poster',
        ),
    ]