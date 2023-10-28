from django.contrib import admin
from .models import Trader, Tracker, CustomUser, MyUserModel
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
#     *UserAdmin.fieldsets,
#     (
#         "Custom Fields",
#         {
#             "fields": ('email', 'age', 'profile_picture'),  # Include the desired fields here
#         },
#     ),
)

add_fieldsets = (
    (
        None,
        {
            "classes": ("wide",),
            "fields": ('username', 'password1', 'password2'),  # Include the desired fields here
        },
    ),
    (
        "Custom Fields",
        {
            "fields": ('email', 'username', 'password'),  # Include the desired fields here
        },
    ),
)


list_display = ("username", "email", "first_name", "last_name", "is_staff")
search_fields = ("username", "email", "first_name", "last_name")
ordering = ("username",)


admin.site.register(Trader)
admin.site.register(Tracker)
admin.site.register(CustomUser, CustomUserAdmin)
