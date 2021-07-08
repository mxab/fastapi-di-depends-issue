
from typing import Callable, Dict, List, Optional, Protocol
from fastapi import Depends, FastAPI
from fastapi.param_functions import Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer

from fastapi import Depends, FastAPI, HTTPException, Security, status
security = HTTPBasic()


bearer = HTTPBearer(bearerFormat="JWT", scheme_name="MyJwt")



class UserDetailExtractor(Protocol):
    def __call__(self,oauth_header: HTTPAuthorizationCredentials) -> Dict[str,any]:
        ...
    
def auth_factory(scope: str, extractor: UserDetailExtractor) -> Callable[[HTTPAuthorizationCredentials], str]:

    def user_if_scope(
        oauth_header:HTTPAuthorizationCredentials = Security(bearer),
    ) -> str:

        # .... extract some token
        user_details = extractor(oauth_header)

        if scope in user_details["scopes"]:
            return user_details

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    
    return user_if_scope