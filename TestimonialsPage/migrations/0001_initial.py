# Generated by Django 4.2.6 on 2023-10-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Randomtext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('auther', models.CharField(max_length=350, verbose_name='auther')),
            ],
        ),
    ]
