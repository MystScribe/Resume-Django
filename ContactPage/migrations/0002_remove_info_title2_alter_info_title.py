# Generated by Django 4.2.6 on 2023-10-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='title2',
        ),
        migrations.AlterField(
            model_name='info',
            name='title',
            field=models.CharField(max_length=350, verbose_name='title(Latest Tweets)'),
        ),
    ]
