from django.contrib import admin

# Register your models here.

from . import models

# 1 Варіант реєстрації(обидва еквівалентні, але 2 ліпше)

class WordAdmin(admin.ModelAdmin):

    list_display = ['pk', 'gender', 'word']
    list_editable = ['gender', 'word']

admin.site.register(models.Word, WordAdmin)


# 2 Варіант реєстрації

# @admin.register(models.Word)
# class WordAdmin(admin.ModelAdmin):
    
#     list_display = ['pk', 'gender', 'word']
#     list_editable = ['gender', 'word']