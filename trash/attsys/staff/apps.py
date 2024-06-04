from django.apps import AppConfig


class StaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staff'  # Update with your new app name
    verbose_name = 'Staff Management'  # Optional: Set a human-readable name
