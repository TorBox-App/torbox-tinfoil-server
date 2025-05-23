import httpx
from library.torbox import TORBOX_API_KEY, TORBOX_API_URL
import logging
import traceback


async def getDownloads(type: str):
    """
    Gets a download type list from TorBox.

    Requires:
    - type: the download type to be retrieved, either "torrents", "usenet", or "webdl"

    Returns:
    - file_list: a list containing all of the files retrieved from the TorBox API.
    """

    if type not in ["torrents", "usenet", "webdl"]:
        logging.error(
            "Please provide a type of either 'torrents', 'usenet' or 'webdl'."
        )
        return []

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=f"{TORBOX_API_URL}/{type}/mylist",
                headers={
                    "Authorization": f"Bearer {TORBOX_API_KEY}",
                    "User-Agent": "TorBox SelfHosted Tinfoil Server/1.0.0",
                },
            )
        if response.status_code != httpx.codes.OK:
            logging.error(
                f"Unable to retrieve TorBox {type} downloads. Response Code: {response.status_code}. Response: {response.json()}"
            )
            return []
        files = []
        json = response.json()
        for download in json.get("data", {}):
            # only get downloads that are completely ready for download
            if not download.get("download_present", False):
                continue
            id = download.get("id", None)
            for file in download.get("files", []):
                if not file.get("s3_path", None):
                    continue
                try:
                    files.append(
                        {
                            "type": type,
                            "id": id,
                            "file_id": file.get("id", 0),
                            "name": file.get("s3_path", None).split("/")[
                                -1
                            ],  # gets only the filename of the file
                            "size": file.get("size", 0),
                        }
                    )
                except Exception as e:
                    logging.error(
                        f"There was an error trying to add {type} download file to file list. Error: {str(e)}"
                    )
                    continue
        return files
    except Exception as e:
        traceback.print_exc()
        logging.error(
            f"There was an error getting {type} downloads from TorBox. Error: {str(e)}"
        )
        return []


async def getDownloadLink(download_type: str, download_id: int, file_id: int = 0):
    if download_type not in ["torrents", "usenet", "webdl"]:
        logging.error(
            "Please provide a type of either 'torrents', 'usenet' or 'webdl'."
        )
        return None

    try:
        async with httpx.AsyncClient() as client:
            if download_type == "torrents":
                id_type = "torrent_id"
            elif download_type == "usenet":
                id_type = "usenet_id"
            elif download_type == "webdl":
                id_type = "web_id"
            params = {"token": TORBOX_API_KEY, id_type: download_id, file_id: file_id}
            response = await client.get(
                url=f"{TORBOX_API_URL}/{download_type}/requestdl",
                params=params,
                headers={"User-Agent": "TorBox SelfHosted Tinfoil Server/1.0.0"},
            )
        if response.status_code != httpx.codes.OK:
            logging.error(
                f"Unable to retrieve TorBox {download_type} download link. Response Code: {response.status_code}. Response: {response.json()}"
            )
            return None

        json = response.json()
        link = json.get("data", None)
        return link
    except Exception as e:
        logging.error(
            f"There was an error retrieving the download url from TorBox. Error: {str(e)}"
        )
