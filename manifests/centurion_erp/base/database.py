DATABASES = {
  'default': {
    'ENGINE': 'django_prometheus.db.backends.postgresql',
    'NAME': 'centurion',                                     # Database name
    'USER': '',                                              # PostgreSQL username
    'PASSWORD': '',                                          # PostgreSQL password
    'HOST': '',                                              # Database server
    'PORT': '',                                              # Database port (leave blank for default)
    'CONN_MAX_AGE': 300,                                     # Max database connection age
  }
}
