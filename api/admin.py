from django.contrib import admin
from .models import Bill, User, Pocket
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'password']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'create_user', 'isCalc', 'date', 'title', 'amount', 'pocket', 'category', 'subcategory', 'memo')

class PocketAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_user', 'category', 'name', 'amount')

admin.site.register(User, UserAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Pocket, PocketAdmin)
