"""
Gitlab Registry

Documentation:
https://docs.gitlab.com/ee/api/packages.html

List packages:
- GET /projects/:id/packages

"""
from app import setup_path

setup_path()

from plugin_manager.services import PackageService


if __name__ == "__main__":
    PROJECT_ID: str = '39007614'
    res: list = PackageService.list_remote_packages(PackageService.get_list_remote_packages_url(PROJECT_ID))
    print(res)
