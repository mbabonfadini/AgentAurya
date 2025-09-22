import os
import dotenv
dotenv.load_dotenv()
from . import BASE_DIR

STATIC_URL = 'static/'
STATIC_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'