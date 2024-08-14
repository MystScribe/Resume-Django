from django.contrib import admin
from .models import EDUCATION, WORK, SKILLS, SkiilsDescription, MoreText

@admin.register(EDUCATION)
class EDUCATIONAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', )


@admin.register(WORK)
class WORKAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', )

@admin.register(SKILLS)
class SKILLSAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', )

@admin.register(SkiilsDescription)
class SkiilsDescriptionAdmin(admin.ModelAdmin):
    list_display = ('description', )

@admin.register(MoreText)
class MoreTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )





