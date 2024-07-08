import uvicorn
from fastapi import FastAPI, HTTPException, status, Depends, Header, Request, BackgroundTasks
from fastapi.responses import JSONResponse
from typing_extensions import Annotated, Union
from library.tinfoil import errorMessage
from library.server import PORT
from functions.authFunctions import checkCorrectCredentials
from functions.serverFunctions import checkAllowed
import logging
from functions.tinfoilFunctions import generateIndex, serveFile

app = FastAPI()
logging.basicConfig(level=logging.INFO)

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
    request: Request,
    authenticated: bool = Depends(checkCorrectCredentials),
    uid: Annotated[Union[str, None], Header()] = None
):
    logging.info(f"Request from Switch with UID: {uid}")
    allowed, response = checkAllowed(authenticated=authenticated, switch_uid=uid)
    if not allowed:
        return JSONResponse(
            content=response,
            status_code=401
        )
    return await generateIndex(base_url=request.base_url)

@app.get("/{download_type}/{download_id}/{file_id}")
async def get_file(
    background_task: BackgroundTasks, # background_task is used to clean up the httpx response afterwards to prevent leakage
    download_type: str,
    download_id: int,
    file_id: int = 0
):
    return await serveFile(background_task=background_task, download_type=download_type, download_id=download_id, file_id=file_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)