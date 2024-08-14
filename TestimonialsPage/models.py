from django.db import models

class quotation(models.Model):
    description = models.TextField(verbose_name='description')
    auther = models.CharField(max_length=350, verbose_name='auther')


