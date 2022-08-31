"""
Documentation:
https://docs.gitlab.com/ee/user/packages/generic_packages/index.html

Publish API:
- PUT /projects/:id/packages/generic/:package_name/:package_version/:file_name?status=:status

"""
import io
import os
from pathlib import Path
import shutil
import zipfile
import requests
from urllib import response


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


if __name__ == "__main__":
    OUTPUT_DIR: str = 'plugins/hello'
    PROJECT_ID: str = '39007614'
    PACKAGE_NAME: str = 'hello'
    PACKAGE_VERSION: str = '0.0.2'
    FILE_NAME: str = 'hello.zip'
    DOWNLOAD_API_URL: str = f'https://gitlab.com/api/v4/projects/{PROJECT_ID}/packages/generic/{PACKAGE_NAME}/{PACKAGE_VERSION}/{FILE_NAME}'

    download_package(DOWNLOAD_API_URL, OUTPUT_DIR)
