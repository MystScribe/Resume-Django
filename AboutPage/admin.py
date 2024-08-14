from django.contrib import admin
from .models import aboutme, Update_Resume
from django.utils.html import mark_safe

@admin.register(aboutme)
class aboutmeAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'img_preview', )

    def img_preview(self, obj):
        return mark_safe(f'<img src = "{obj.image.url}" width = "150" height= "150" />')


admin.site.register(Update_Resume)

