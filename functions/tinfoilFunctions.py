import asyncio
from functions.torboxFunctions import getDownloads
import logging
from library.tinfoil import errorMessage
from fastapi.responses import JSONResponse

ACCEPTABLE_SWITCH_FILES = [".nsp", ".nsz", ".xci", ".xcz"]


async def generateIndex(base_url: str):
    """
    Generates a JSON index from your TorBox files. Matches only switch compatible files and returns a well-formatted JSON index for Tinfoil.

    Requires:
    - base_url: where the server is hosted, so it can create proper URLs.

    Returns:
    - dict: the generated index for Tinfoil to use.
    """

    success_message = "Welcome to your self-hosted TorBox Tinfoil Server! You are now able to directly download your files from TorBox to your switch.\n\n"
    files = []
    try:
        # runs all requests in parallel for faster responses
        torrents, usenet_downloads, web_downloads = await asyncio.gather(getDownloads("torrents"), getDownloads("usenet"), getDownloads("webdl"))
        
        file_list = torrents + usenet_downloads + web_downloads


    except Exception as e:
        logging.error(f"There was an error generating the index. Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=errorMessage(f"There was an error generating the index. Error: {str(e)}", error_code="UNKOWN_ERROR")
        )



            
