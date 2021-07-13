from dependency_injector.containers import DeclarativeContainer
from dependency_injector import providers
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBasic


class Container(DeclarativeContainer):
    config = providers.Configuration()
    bearer  = providers.Singleton(HTTPBasic, auto_error=config.secured.as_(bool))