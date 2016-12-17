from django.contrib import admin
from main.models import HypoUser


class AdminHypoUser(admin.ModelAdmin):
    list_display = ['user', 'counter']

    class Meta:
        model = HypoUser

admin.site.register(HypoUser, AdminHypoUser)
