from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Display field for blog page
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
