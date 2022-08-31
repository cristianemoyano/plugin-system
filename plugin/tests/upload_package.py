"""
Gitlab Registry

Documentation:
https://docs.gitlab.com/ee/user/packages/generic_packages/index.html

Publish API:
- PUT /projects/:id/packages/generic/:package_name/:package_version/:file_name?status=:status

"""
from app import setup_path
from urllib import response

setup_path()

from plugin_manager.services import PackageService


if __name__ == "__main__":
    PATH_FILE: str = 'hello.zip'
    PROJECT_ID: str = '39007614'
    PACKAGE_NAME: str = 'hello'
    PACKAGE_VERSION: str = '0.0.2'
    FILE_NAME: str = 'hello.zip'
    UPLOAD_API_URL: str = f'https://gitlab.com/api/v4/projects/{PROJECT_ID}/packages/generic/{PACKAGE_NAME}/{PACKAGE_VERSION}/{FILE_NAME}'

    res: response = PackageService.upload_package(UPLOAD_API_URL, PATH_FILE)
    print(res.content)
