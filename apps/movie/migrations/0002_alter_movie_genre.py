# Generated by Django 4.0.5 on 2022-07-01 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(max_length=80, on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Genre'),
        ),
    ]