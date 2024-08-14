from django.db import models



class intruduce(models.Model):
    title = models.CharField(max_length=350, verbose_name='title')
    description = models.TextField(verbose_name='description')
    facebook = models.CharField(max_length=500, verbose_name='facebook')
    twitter = models.CharField(max_length=500, verbose_name='twitter')
    googleplus = models.CharField(max_length=500, verbose_name='googleplus')
    linkedin = models.CharField(max_length=500, verbose_name='linkedin')
    instagram = models.CharField(max_length=500, verbose_name='instagram')
    skype = models.CharField(max_length=500, verbose_name='skype')
