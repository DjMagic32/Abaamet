from django.contrib import admin
from user.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Cargos',
            {
                'fields': (
                    'is_Ventas',
                    'is_Metrologia',
                    'is_Direccion',
                    'is_Compras',
                )
            }
        )
    )

admin.site.register(User, CustomUserAdmin)