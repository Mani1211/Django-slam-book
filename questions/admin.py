from django.contrib import admin
from .models import Questions

# Register your models here.

class QuestionsAdmin(admin.ModelAdmin):
    list_display=('id','name','number','weakness','advice','positive','like','words','memory')
admin.site.register(Questions,QuestionsAdmin)