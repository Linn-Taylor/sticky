from pathlib import Path

# 全体の設定
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

DEBUG = True
LANGUAGE_CODE = "ja"
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'index'
# LOGOUT_REDIRECT_URL = LOGIN_URL
SECRET_KEY = "django-insecure-!!a7=hwm7s6hejw7l!lby!4!2l*oc8jb51okjtg&pgauy=ihup"
WSGI_APPLICATION = "sticky.wsgi.application"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_L10N = True
USE_TZ = False

# URL/PATHの設定
ALLOWED_HOSTS = []
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
ROOT_URLCONF = "sticky.urls"
# STATIC_URL = "/static"

# INstallApps

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main.apps.MainConfig",
    "note.apps.NoteConfig",
    "macro.apps.MacroConfig",
]

# Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database
# AUTH_USER_MODEL = "main.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASE_ROUTERS = ["sticky.db.DbRouter"]

DATABASES = {
    "default": {},
    "main": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "main/main.sqlite3",
        "TEST": {"DEPENDENCIES": []},
    },
    "note": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "note/note.sqlite3",
        "TEST": {"DEPENDENCIES": ["main"]},
    },
    "macro": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "macro/macro.sqlite3",
        "TEST": {"DEPENDENCIES": ["main"]},
    },
}
