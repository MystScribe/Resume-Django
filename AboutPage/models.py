from django.db import models
from django import forms

class aboutme(models.Model):
    Aboutme = models.CharField(max_length=350, verbose_name='Title(Aboutme)')
    DescriptionAboutme = models.TextField(verbose_name='Description(Aboutme)')
    ContactDetails = models.CharField(max_length=350, verbose_name='Title(ContactDetails)')
    Name = models.CharField(max_length=350, verbose_name='Name')
    Address = models.CharField(max_length=350, verbose_name='Address')
    PhoneNumber = models.CharField(max_length=350, verbose_name='PhoneNumber')
    Email = models.EmailField(max_length=350, verbose_name='Email')
    image = models.ImageField(upload_to='media', verbose_name='profile', default='pic')

class Update_Resume(models.Model):
    Resume = models.FileField(upload_to='static/media', verbose_name='Resume File')

