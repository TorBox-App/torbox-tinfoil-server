import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.security import HTTPBasic
from fastapi.responses import JSONResponse

from library.tinfoil import errorMessage
from library.server import PORT

app = FastAPI()
security = HTTPBasic()

# Custom exemption handler to be well-formatted with Tinfoil so the user knows what has happened if no authentication is sent, as it is required.
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=errorMessage(message="Please authenticate using your username and password set when the server was created.", error_code="NO_AUTH"),
        )
    return await request.app.exception_handler(exc)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)