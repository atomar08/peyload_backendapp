from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from peyload.models import Account

# admin.site.register(Account)

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_no', 'date_joined', 'last_login')
    search_fields = ('email', 'first_name', 'last_name', 'phone_no', 'date_joined',)
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('email', 'first_name', 'last_name', 'phone_no', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter= ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)