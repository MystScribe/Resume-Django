# Generated by Django 4.2.6 on 2023-10-27 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResumePage', '0004_rename_txt_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='kore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.DeleteModel(
            name='description',
        ),
    ]
