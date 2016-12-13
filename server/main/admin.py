from django.contrib import admin
from main.models import HypoUser


class AdminHypoUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'name']

    class Meta:
        model = HypoUser

admin.site.register(HypoUser, AdminHypoUser)
