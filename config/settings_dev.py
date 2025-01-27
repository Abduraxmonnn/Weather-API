from config.settings import *

IS_DEV = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DJANGO DEBUG TOOLBAR
INTERNAL_IPS = [
    "127.0.0.1",
]
