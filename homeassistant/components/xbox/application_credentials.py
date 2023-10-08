"""Application credentials platform for xbox."""

from homeassistant.components.application_credentials import AuthorizationServer

from .const import OAUTH2_AUTHORIZE, OAUTH2_TOKEN


async def async_get_authorization_server() -> AuthorizationServer:
    """Return authorization server."""
    return AuthorizationServer(
        authorize_url=OAUTH2_AUTHORIZE,
        token_url=OAUTH2_TOKEN,
    )
