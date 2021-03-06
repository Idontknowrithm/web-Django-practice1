from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name',  'email')
    
admin.site.register(User, UserAdmin)