from django.contrib import admin
from django.contrib.auth.models import User

from finance.models import Organization, UserType
#
# class OrganizationInline(admin.TabularInline):
#     model = Organization

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'last_login', 'is_staff', 'is_superuser']
    # inlines = [OrganizationInline]

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# admin.site.unregister(User)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(UserType, UserTypeAdmin)
# admin.site.register(User, CustomUserAdmin)
