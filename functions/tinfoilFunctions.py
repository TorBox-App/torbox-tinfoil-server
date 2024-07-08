import asyncio
from functions.torboxFunctions import getDownloads
import logging
from library.tinfoil import errorMessage
from fastapi.responses import JSONResponse
import fnmatch
import human_readable

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

        for file in file_list:
            file_name = file.get("name", None)
            download_type = file.get("type")
            download_id = file.get("id")
            file_id = file.get("file_id", 0)


            for acceptable_file_type in ACCEPTABLE_SWITCH_FILES:
                if fnmatch.fnmatch(file_name, f"*{acceptable_file_type}"):
                    # create a url for the download
                    files.append({
                        # example base_url = http://192.168.0.1/
                        # example complete_url = http://192.168.0.1/torrents/1/1#Game_Name
                        "url": f"{base_url}{download_type}/{download_id}/{file_id}#{file_name}",
                        "size": file.get("size", 0)
                    })

        success_message += f"Total Files: {len(files)}"
        success_message += f"\nTotal Size: {human_readable.file_size(sum([file.get('size', 0) for file in files]))}"
        return JSONResponse(
            status_code=200,
            content={
                "success": success_message,
                "files": files
            }
        )
    except Exception as e:
        logging.error(f"There was an error generating the index. Error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content=errorMessage(f"There was an error generating the index. Error: {str(e)}", error_code="UNKOWN_ERROR")
        )



            
