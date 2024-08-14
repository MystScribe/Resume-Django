from django.contrib import admin
from .models import intruduce

@admin.register(intruduce)

class intruduceAdmin(admin.ModelAdmin):
    list_display = ('title', )
