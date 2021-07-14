from fastapi import FastAPI, Depends, Request
from fastapi.security.http import HTTPBasic, HTTPBasicCredentials
from dependency_injector.wiring import Provide, inject
from fastapi_di_depends_issue.container import Container

app = FastAPI()

#### working
fixed_bearer = HTTPBasic()


@app.get("/fixed")
def fixed(user: HTTPBasicCredentials = Depends(fixed_bearer)):

    return {"username": user.username}


#### not working
di_bearer = Provide[Container.bearer]


@app.get("/with_di")
@inject
def with_di(user: HTTPBasicCredentials = Depends(di_bearer)):

    return {"username": user.username if user else None}


@inject
async def workarround(
    request: Request, di_bearer=Depends(Provide[Container.bearer])
) -> HTTPBasicCredentials:

    return await di_bearer(request)


@app.get("/with_di_workarround")
@inject
def with_di_workarround(user: HTTPBasicCredentials = Depends(workarround)):

    return {"username": user.username if user else None}
