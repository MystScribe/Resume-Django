from django.db import models

class info(models.Model):
    description = models.TextField(verbose_name='description')



class descrip(models.Model):
    description = models.TextField(verbose_name='description')
    date = models.DateField(max_length=350, verbose_name='date')

class Copyright(models.Model):
    firstcopyright = models.CharField(max_length=350, verbose_name='copyrights 1', default='COPYRIGHT')
    secondcopyright = models.CharField(max_length=350, verbose_name='copyrights 2', default='COPYRIGHT')


class ContactUsReceiveForm(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name')
    email = models.EmailField(max_length=250, verbose_name='Email')
    subject = models.CharField(max_length=250, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')



