from django.contrib import admin
from ausers.models import CustomUser, UserConfirmation


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserConfirmation)
class UserConfirmationAdmin(admin.ModelAdmin):
    pass
