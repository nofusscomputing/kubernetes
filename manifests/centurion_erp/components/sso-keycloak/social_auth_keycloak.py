LOGIN_URL = '/sso/login/keycloak/'
LOGOUT_REDIRECT_URL = "/sso/login/keycloak/"

SOCIAL_AUTH_KEYCLOAK_KEY = ''           # Keycloak oidc id
SOCIAL_AUTH_KEYCLOAK_SECRET = ''        # oidc secret key
SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY = ''    # public key
SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL = 'https://<domain.tkd>/realms/<realm name>/protocol/openid-connect/auth'
SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL = 'https://<domain.tkd>/realms/<realm name>/protocol/openid-connect/token'

SSO_ENABLED = True

SSO_BACKENDS = (
  "social_core.backends.keycloak.KeycloakOAuth2",
  # "social_core.backends.open_id_connect.OpenIdConnectAuth",
)
