import requests
import json


class YandexUploader:
    _upload_folder_path: str = "/UploadFolder"

    def __init__(self, hostname: str, access_token: str ):
        self._hostname = f"{hostname}/v1/disk"

        self._access_token = access_token
        self._authorization_header = {
            "Authorization": self._access_token
        }

    def _get_upload_link(self) -> str:
        """
            Method used for getting a unique link for uploading our file
        :return: Unique link which will be used for uploading file
        """

        return json.loads(requests.get(
            url=f"{self._hostname}/resources/upload",
            headers=self._authorization_header,
            params={
                "path": f"{self._upload_folder_path}/",
                'overwrite': "true"
            }
        ).content).get('href')

    def upload_file(self, file_path: str) -> int:
        """
            Method used for uploading file from local machine
        :param file_path: Full path to the file stored on the local machine
        :return: Response status code from API endpoint
        """

        return requests.put(
                url=self._get_upload_link(),
                data=open(file_path, "rb")
            ).status_code
