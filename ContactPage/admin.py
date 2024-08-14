from django.contrib import admin
from .models import info, Copyright, descrip, ContactUsReceiveForm

@admin.register(info)
class infoAdmin(admin.ModelAdmin):
    list_display = ('description', )

@admin.register(Copyright)
class CopyrightAdmin(admin.ModelAdmin):
    list_display = ('firstcopyright', 'secondcopyright', )

@admin.register(descrip)
class descripAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', )

@admin.register(ContactUsReceiveForm)
class ContactUsReceiveFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', )
