from django.apps import AppConfig

VERBOSE_APP_NAME = '查询'
class QueryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'query'
    verbose_name = VERBOSE_APP_NAME
