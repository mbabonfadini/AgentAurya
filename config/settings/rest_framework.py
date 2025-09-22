import os
import dotenv
dotenv.load_dotenv()

DEBUG = os.getenv('DEBUG', 'False') == 'True'

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


