# Generated by Django 4.2.6 on 2023-10-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='link',
        ),
        migrations.AlterField(
            model_name='header',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
    ]
