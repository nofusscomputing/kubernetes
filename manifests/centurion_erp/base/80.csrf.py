SITE_URL = 'https://<domain.tld>'

TRUSTED_ORIGINS = [
  'https://<domain.tld>',
  'https://<sub-domain.domain.tld>',
]

# SSL
SECURE_SSL_HOST = '<domain.tld>'
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

USE_X_FORWARDED_HOST = True
SESSION_COOKIE_SECURE = True
