from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ExportActionModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Career


class UserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "created_at")

        export_order = ("username", "email", "created_at")


class CustomUserAdmin(ExportActionModelAdmin, UserAdmin):
    """
    Configure the users app in admin app
    """

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    resource_class = UserResource
    model = CustomUser
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2",),
            },
        ),
        (_("Permissions"), {"fields": ("is_superuser", "is_staff")}),
    )

    fieldsets = (
        (None, {"fields": ("username", "password", "is_customer", "is_worker", "careers")}),
        (_("Personal info"), {"classes": ("collapse",), "fields": ("email", "full_name", "phone_number", "picture")},),
        (
            _("Permissions"),
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {"classes": ("collapse",), "fields": ("last_login", "date_joined")},
        ),
    )

    list_display = (
        "username",
        "email",
        "is_active",
        "is_customer",
        "is_worker",
    )

    list_filter = ("is_customer", "is_worker", "last_login")

    date_hierarchy = "date_joined"


class CareerHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["name"]
    search_fields = ['name']


admin.site.site_title = _("MLRecruiters site admin")
admin.site.site_header = _("MLRecruiters Dashboard")
admin.site.index_title = _("Welcome to MLRecruiters")
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Career, CareerHistoryAdmin)
