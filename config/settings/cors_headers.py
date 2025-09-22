from .environment import DEBUG

ALLOWED_HOSTS = ['*']

SESSION_COOKIE_SECURE = not DEBUG   # só HTTPS
SESSION_COOKIE_HTTPONLY = True     # não acessível via JS
SESSION_COOKIE_SAMESITE = "Lax"