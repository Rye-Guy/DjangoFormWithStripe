from .settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ALLOWED_HOSTS = ['159.203.12.224', 'localhost', '127.0.0.1']


SECRET_KEY = 'm#=^9pi0f-lm_v_zbki)$62$%ht1w^b#*fq%bzk$gq1+e17jz+'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = '/var/www/static-root/'
MEDIA_ROOT = '/var/www/media-root/'