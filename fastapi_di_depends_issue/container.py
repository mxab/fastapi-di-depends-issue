from dependency_injector.containers import DeclarativeContainer
from dependency_injector import providers
from fastapi.security.http import HTTPAuthorizationCredentials


def some_di_extractor(some_config: str, oauth_header:HTTPAuthorizationCredentials):
    return {
            "username": "bar",
            "scopes": ["read", "write"]
        }

class Container(DeclarativeContainer):

    user_detail_extractor = providers.Callable(some_di_extractor, some_config="bla") # real world some more parameter