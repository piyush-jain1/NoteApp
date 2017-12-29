from django.contrib import admin
from django.conf import settings
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('username','phone')
	search_field = ['phone']

admin.site.register(User,UserAdmin)
