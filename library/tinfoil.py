import os
from dotenv import load_dotenv
load_dotenv()

SWITCH_UID = os.getenv("SWITCH_UID", None)


def errorMessage(message: str, error_code: str):
    """
    Simply returns a well-formatted error message that works with Tinfoil.

    Requires:
    - message: a string which contains a human-readable message to the user about what went wrong.
    - error_code: a string which is a documented error code for a developer to know. For error code documenation, view here: https://api-docs.torbox.app

    Returns:
    - error: a dict with the 'error' key which is read by Tinfoil. Documentation here: https://blawar.github.io/tinfoil/custom_index/
    """
    
    return {
        "error": f"TorBox\n\n{message}\n\nError: {error_code}"
    }