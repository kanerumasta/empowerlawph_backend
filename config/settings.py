
from pathlib import Path
from os import getenv, path
import dotenv
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = BASE_DIR / '.env.local'

if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fu((!8w#8vy0dw$j2t9_77_p2ivcwo$093lx@x)y)ry0@-7lxd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '10.160.153.57',
    '10.160.153.131'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'djoser',

    'accounts',
    'case',
    'search',
    'highlight',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://10.160.153.163:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=360),
}


DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'LOGIN FIELD' : 'email',
    "PERMISSIONS": {
        "user_create": ["rest_framework.permissions.AllowAny"],
    }
    # 'ACTIVATION_URL': 'activate/{uid}/{token}',
    # 'SEND_ACTIVATION_EMAIL': True,

}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Example for Gmail
EMAIL_PORT = 587  # For Gmail and most SMTP servers
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'empowerlawph@gmail.com'
EMAIL_HOST_PASSWORD = 'tzqi qvnz jsks xeox'

DEFAULT_FROM_EMAIL = 'empowerlawph@innodata.com'
SITE_NAME = 'EmpowerLawPH'
DOMAIN = '127.0.0.1:3000'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
     'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'empowerlawph_DB',
        'USER': 'postgres',
        'PASSWORD': '011456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Enter: **Bearer <JWT Token>**",
        }
    },
    "USE_SESSION_AUTH": False,  # Disable Django session authentication in Swagger UI
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

AUTH_COOKIE = 'access'
AUTH_COOKIE_ACCESS_MAX_AGE = 60 * 60
AUTH_COOKIE_REFRESH_MAX_AGE = 60 * 60 *24
AUTH_COOKIE_SECURE = False #change in production
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'strict'
