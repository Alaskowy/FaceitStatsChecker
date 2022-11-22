from django.contrib import admin

from .models import Account


class AdminAccount(admin.ModelAdmin):
    list_display = ('email', 'faceit_account')


admin.site.register(Account, AdminAccount)