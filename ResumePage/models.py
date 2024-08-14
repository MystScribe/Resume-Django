from django.db import models

class EDUCATION(models.Model):
    title = models.CharField(max_length=350, verbose_name='title')
    degree = models.CharField(max_length=350, verbose_name='degree')
    date = models.DateField(max_length=350, verbose_name='date')
    description = models.TextField( verbose_name='description')





class WORK(models.Model):

    title = models.CharField(max_length=350, verbose_name='title')
    degree = models.CharField(max_length=350, verbose_name='Job')
    date = models.DateField(max_length=350, verbose_name='date')
    description = models.TextField( verbose_name='description')


class SkiilsDescription(models.Model):
    description = models.TextField(verbose_name='description')

class SKILLS(models.Model):
    title = models.CharField(max_length=350, verbose_name='title')
    rate = models.IntegerField(default=0, verbose_name='rate')

class MoreText(models.Model):
    title = models.CharField(max_length=350, verbose_name='title')
    description = models.TextField( verbose_name='description')
