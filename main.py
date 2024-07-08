import uvicorn
from fastapi import FastAPI, HTTPException, status, Depends, Header
from fastapi.responses import JSONResponse
from typing_extensions import Annotated, Union
from library.tinfoil import errorMessage
from library.server import PORT
from functions.authFunctions import checkCorrectCredentials
from functions.serverFunctions import checkAllowed

app = FastAPI()

# Custom exemption handler to be well-formatted with Tinfoil so the user knows what has happened if no authentication is sent, as it is required.
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=errorMessage(message="Please authenticate using your username and password set when the server was created.", error_code="NO_AUTH"),
        )
    return await request.app.exception_handler(exc)

@app.get("/")
async def get_user_files(
    authenticated: bool = Depends(checkCorrectCredentials),
    uid: Annotated[Union[str, None], Header()] = None
):
    allowed, response = checkAllowed(authenticated=authenticated, switch_uid=uid)
    if not allowed:
        return JSONResponse(
            content=response,
            status_code=401
        )
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)