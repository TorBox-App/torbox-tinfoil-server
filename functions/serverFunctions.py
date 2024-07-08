from library.tinfoil import errorMessage, SWITCH_UID


def checkAllowed(authenticated: bool, switch_uid: str):
    """
    Checks if a user should be allowed to finish the request, otherwise returns an error message.

    Requires:
    - authenticated: a boolean which tells the server if the user is authenticated or not.
    - switch_uid: a string which either contains a uid or not. If no UID then a user is not using a switch. Also has the ability to check if the switch UID matches the required UID.

    Returns:
    - boolean, dict: the boolean determines if the user is allowed past, the dict gives the errorMessage.
    """

    if not authenticated:
        return False, errorMessage(
            "Your given credentials are incorrect. Please try again.",
            error_code="BAD_TOKEN",
        )
    if not switch_uid:
        return False, errorMessage(
            "Please use your Nintendo Switch using Tinfoil to access this server.",
            error_code="INVALID_DEVICE",
        )
    if SWITCH_UID and switch_uid != SWITCH_UID:
        return False, errorMessage(
            "This switch is not authorized to use this server. Please use the correct switch to access.",
            error_code="INVALID_DEVICE",
        )

    return True, None
