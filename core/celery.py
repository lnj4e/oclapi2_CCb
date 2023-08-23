import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery('core')
app.conf.ONCE = {
    'backend': 'core.common.backends.QueueOnceRedisBackend',
    'settings': {}
}
app.conf.CELERYBEAT_SCHEDULE = {
    'healthcheck-every-minute': {
        'task': 'core.common.tasks.beat_healthcheck',
        'schedule': timedelta(seconds=60),
    },
    'first-of-every-month': {
        'task': 'core.common.tasks.monthly_usage_report',
        'schedule': crontab(1, 0, day_of_month='1'),
    },
    'vacuum-and-analyze-db': {
        'task': 'core.common.tasks.vacuum_and_analyze_db',
        'schedule': crontab(0, 1),  # Run at 1 am
    },

}
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
