from django.contrib import admin
from .models import User  # Import your User model here

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','bio']

# Register the User model with the admin site
admin.site.register(User, UserAdmin)
