from django.contrib import admin
from main.models import HypoUser


class AdminHypoUser(admin.ModelAdmin):
    list_display = ['username', 'email']

    class Meta:
        model = HypoUser

admin.site.register(HypoUser, AdminHypoUser)
