from django.contrib import admin
from .models import quotation

@admin.register(quotation)
class quotationAdmin(admin.ModelAdmin):
    list_display = ('auther', )

