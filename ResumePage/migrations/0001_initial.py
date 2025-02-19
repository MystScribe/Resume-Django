# Generated by Django 4.2.6 on 2023-10-27 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EDUCATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('degree', models.CharField(max_length=350, verbose_name='degree')),
                ('date', models.DateField(max_length=350, verbose_name='date')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='SKILLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('rate', models.IntegerField(default=0, verbose_name='rate')),
            ],
        ),
        migrations.CreateModel(
            name='txt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='WORK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='title')),
                ('degree', models.CharField(max_length=350, verbose_name='degree')),
                ('date', models.DateField(max_length=350, verbose_name='date')),
                ('description', models.TextField(verbose_name='description')),
                ('EDUCATION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ResumePage.education')),
            ],
        ),
    ]
