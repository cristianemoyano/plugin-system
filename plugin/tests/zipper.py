from app import setup_path

setup_path()

from plugin_manager.services import PackageService

if __name__ == "__main__":
    PackageService.zip_package('hello', 'plugins/hello')
