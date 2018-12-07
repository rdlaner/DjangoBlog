import os
import dj_database_url
import settings

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(settings.BASE_DIR, 'db.sqlite3'))
}

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
STATIC_ROOT = os.path.join(settings.BASE_DIR, 'static')
SECRET_KEY = os.environ.get('SECRET_KEY')
