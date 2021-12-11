import os

SECRET_KEY = '^l)7d*%h&db4uft@dk%h-w&nup#pu%)a!d)c7jwgoixo5_hm0$'

DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'autenticacion.USUARIO'

INSTALLED_APPS = [
    'jazzmin',
    'rolepermissions',
    'dj_pagination',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.estructura',
    'apps.contratacion',
    'apps.autenticacion',
    'apps.publico',
    'apps.postulantes',
    'import_export',
]

MIDDLEWARE = [
    'dj_pagination.middleware.PaginationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Apolo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'Apolo.wsgi.application'
LOGOUT_REDIRECT_URL = 'login'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'apolo',
        'USER': 'usrApolo',
        'PASSWORD': 'Password',
#        'HOST': '172.18.4.10',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

X_FRAME_OPTIONS = 'SAMEORIGIN'
JAZZMIN_SETTINGS = {
    "site_title": "Apolo",
    "site_header": "Integracion Social",
    "site_logo": "img.png",
    "welcome_sign": "Bienvenido a la plataforma Apolo",
    "copyright": "Secretaria de integracion social",
    "search_model": "auth.User",
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Inicio", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Web", "url": "https://sdis.gov.co", "new_window": True},

        # model admin to link to (Permissions checked against model)
        #   {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "contratacion"}, {"app": "estructura"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"model": "auth.user"},
        {"name": "Tablero de Seguimiento",
         "url": "https://app.powerbi.com/view?r=eyJrIjoiYjAyOWExYTQtMzYwZC00MDdjLThiMDYtNGQ3YjljZTg1YmFiIiwidCI6ImIzZTMwODA4LWU5YTgtNGYyYS05YmMxLWE3NjBhZTkxMGNmNSIsImMiOjR9&pageName=ReportSectiona7c034c1e01ec62a10ef",
         "new_window": True},
        {"name": "Ayuda", "url": "https://sdis.gov.co", "new_window": True},
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "estructura", "estructura.Provincia"],

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "vendor/bootswatch/minty/bootstrap.min.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "carousel",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs", },
    # Add a language dropdown into the admin
    "language_chooser": False,
}

ROLEPERMISSIONS_MODULE = 'Apolo.roles'


#datos de acceso a SIDEAP
SIDEAP_URL = "http://preproduccion.serviciocivil.gov.co:8585/sideapInteroperabilidad/webresourcesJSON/sdis/obtenerDatosBasicosSDIS"
SIDEAP_KEY = "9DBD932AB4D1308A3332C5181B2242F3BDD21408DE201FA2A3C261DE5370BE89"
SIDEAP_USER = "PRUEBAS"
#configuracion correo correoElectronico
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rmoscosop@sdis.gov.co'
EMAIL_HOST_PASSWORD = 'Bogota20'

APOLOHV_URL = 'http://hv.apolo.sdis.gov.co'


