DEBUG = False

# FEATURE_FLAG_OVERRIDES = [
#   {'disable_downloading': False},
# ]

METRICS_ENABLED = True
# PROMETHEUS_EXPORT_MIGRATIONS = True

AUTH_PASSWORD_VALIDATORS = []

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True

USE_X_FORWARDED_HOST = True

LOG_FILES = {
  "catch_all":"/var/log/catch-all.log",
  "centurion_trace": "/var/log/trace.log",
  "centurion": "/var/log/centurion.log",
  "error": "/var/log/error.log",
  "gunicorn": "/var/log/gunicorn.log",
  "rest_api": "/var/log/rest_api.log",
  "weblog": "/var/log/weblog.log",
}
