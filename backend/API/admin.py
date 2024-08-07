from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CUser, Vendor


class CUserAdmin(UserAdmin):
    # Customize how the CustomUser model is displayed in the admin interface
    list_display = ("username", "email", "is_staff", "date_joined")
    list_filter = ("is_staff",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("first_name", "last_name", "email", "user_type")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(CUser, CUserAdmin)
admin.site.register(Vendor)
