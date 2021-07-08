


from fastapi.applications import FastAPI
from fastapi.param_functions import Depends
from fastapi.security.http import HTTPAuthorizationCredentials
from dependency_injector.wiring import Provide, Provider
from fastapi_di_depends_issue.container import Container
from fastapi_di_depends_issue.third_party import auth_factory

app = FastAPI()


def fixed_extractor(oauth_header:HTTPAuthorizationCredentials):
    return {
        "username": "foo",
        "scopes": ["read", "write"]
    }

@app.get("/fixed")
def fixed(user = Depends(auth_factory(scope="read", extractor = fixed_extractor ))):

    return {
        "user": user["username"]
    }



user_detail_extractor = Provide[Container.user_detail_extractor]

@app.get("/with_di")
def with_di(user = Depends(auth_factory(scope="read", extractor = user_detail_extractor ))):

    return {
        "user": user["username"]
    }



