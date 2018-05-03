from django.contrib import admin
from .models import Todo_bord
# Register your models here.

class Todo_bordAdmin(admin.ModelAdmin):
    list_display = ('id','new_message','created_at')

admin.site.register(Todo_bord,Todo_bordAdmin)
