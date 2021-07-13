


from fastapi.applications import FastAPI
from fastapi.param_functions import Depends
from fastapi.security.http import HTTPBasic, HTTPBasicCredentials
from dependency_injector.wiring import Provide
from fastapi_di_depends_issue.container import Container

app = FastAPI()


fixed_bearer = HTTPBasic()
@app.get("/fixed")
def fixed(user: HTTPBasicCredentials = Depends(fixed_bearer)):

    return {"username" : user.username}



di_bearer = Provide[Container.bearer]

@app.get("/with_di")
def with_di(user: HTTPBasicCredentials = Depends(di_bearer)):

    return {"username" : user.username if user else None}


