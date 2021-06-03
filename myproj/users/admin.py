from django.contrib import admin

from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(User, UserAdmin)
