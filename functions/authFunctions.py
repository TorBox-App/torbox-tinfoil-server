from library.server import AUTH_USERNAME, AUTH_PASSWORD
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()


def checkCorrectCredentials(credentials: HTTPBasicCredentials = Depends(security)):
    """
    A simple function that compares the passed credentials to the known correct credentials. Documentation and code from https://fastapi.tiangolo.com/advanced/security/http-basic-auth/#check-the-username

    Requires:
    - credentials: credentials passed from the request.

    Returns:
    - boolean: the boolean determines if the credentials match.
    """


    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = AUTH_USERNAME.encode("utf-8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = AUTH_PASSWORD.encode("utf-8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        return False
    return True
    