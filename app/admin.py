from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser,room_model
from django.utils.translation import gettext_lazy as _
import uuid






@admin.register(room_model)
class room_modelAdmin(admin.ModelAdmin):
    list_display = ['id','room']
    prepopulated_fields = {"slug": ( 'room' ,)}




class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_online",
                    "is_reserved",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ("uu_id","username", "email", "is_online","is_reserved","is_active" ,"is_staff",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(CustomUser,CustomUserAdmin)
