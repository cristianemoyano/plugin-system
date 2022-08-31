import io
import os
from pathlib import Path
import shutil
import zipfile
import requests
from urllib import response


class PackageService:

    @staticmethod
    def download_package(url: str, output_dir:str) -> None:
        destination: Path = Path(output_dir)
        if destination.is_dir():
            # check if directory exists
            shutil.rmtree(destination)

        os.mkdir(output_dir)
        headers: dict = {
            'PRIVATE-TOKEN': os.environ.get('GITLAB_PRIVATE_TOKEN')
        }
        res: response = requests.get(url, headers=headers)
        z: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(res.content))
        z.extractall(path=output_dir)

    @staticmethod
    def upload_package(url: str, path_file: str) -> response:
        headers: dict = {
            'PRIVATE-TOKEN': os.environ.get('GITLAB_PRIVATE_TOKEN')
        }
        fileobj: object = open(path_file, 'rb')
        return requests.put(url, headers=headers, data=fileobj.read())

    @staticmethod
    def zip_package(output_filename: str, dir_name: str) -> None:
        shutil.make_archive(output_filename, 'zip', dir_name)

