"""
Documentation:
https://docs.gitlab.com/ee/user/packages/generic_packages/index.html

Publish API:
- PUT /projects/:id/packages/generic/:package_name/:package_version/:file_name?status=:status

"""
import os
import requests
from urllib import response

def upload_package(url: str, path_file: str) -> response:
    headers: dict = {
        'PRIVATE-TOKEN': os.environ.get('GITLAB_PRIVATE_TOKEN')
    }
    fileobj: object = open(path_file, 'rb')
    return requests.put(url, headers=headers, data=fileobj.read())

if __name__ == "__main__":
    PATH_FILE: str = 'hello.zip'
    PROJECT_ID: str = '39007614'
    PACKAGE_NAME: str = 'hello'
    PACKAGE_VERSION: str = '0.0.2'
    FILE_NAME: str = 'hello.zip'
    UPLOAD_API_URL: str = f'https://gitlab.com/api/v4/projects/{PROJECT_ID}/packages/generic/{PACKAGE_NAME}/{PACKAGE_VERSION}/{FILE_NAME}'

    res: response = upload_package(UPLOAD_API_URL, PATH_FILE)
    print(res.content)
