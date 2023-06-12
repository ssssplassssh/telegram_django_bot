from django.contrib import admin

# Register your models here.

from . import models

# 1 Registration option (both are equivalent, but 2 is better)

class WordAdmin(admin.ModelAdmin):

    list_display = ['pk', 'gender', 'word']
    list_editable = ['gender', 'word']

admin.site.register(models.Word, WordAdmin)


# 2 Registration option
# @admin.register(models.Word)
# class WordAdmin(admin.ModelAdmin):
    
#     list_display = ['pk', 'gender', 'word']
#     list_editable = ['gender', 'word']