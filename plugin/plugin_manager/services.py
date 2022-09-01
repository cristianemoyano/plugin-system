import io
import logging
import os
from pathlib import Path
import shutil
import zipfile
import requests
from urllib import response


from plugin_manager import interface
from plugin_manager import loader

logger: logging.Logger = logging.getLogger(__name__)

class PackageService:

    @staticmethod
    def list_imports(path) -> list:
        dir_list: list[str] = os.listdir(path)
        dir_list.remove('__init__.py')
        return map(lambda directory: f'{path}.{directory}', dir_list)

    @staticmethod
    def list_packages(path) -> list:
        dir_list: list[str] = os.listdir(path)
        dir_list.remove('__init__.py')
        plugin_list: list = []
        for plugin_import in map(lambda directory: f'{path}.{directory}', dir_list):
            try:
                plugin_module: loader.ModuleInterface = loader.import_plugin_module(plugin_import)
            except ModuleNotFoundError as exc:
                logger.exception(f"Something went wrong trying to import the plugin: '{plugin_import}' . Error: {exc}")
                continue
            # Get the main plugin class
            plugin_class: interface.PluginInterface = plugin_module.register()
            plugin_meta: dict[str, str] = interface.get_plugin_metadata(plugin_class)
            plugin_list.append(plugin_meta)
        return plugin_list
    
    @staticmethod
    def get_download_url(project_id: str, package_name: str, package_version: str, file_name: str) -> str:
        return f'https://gitlab.com/api/v4/projects/{project_id}/packages/generic/{package_name}/{package_version}/{file_name}'

    @staticmethod
    def get_upload_url(project_id: str, package_name: str, package_version: str, file_name: str) -> str:
        return f'https://gitlab.com/api/v4/projects/{project_id}/packages/generic/{package_name}/{package_version}/{file_name}'

    @staticmethod
    def download_package(url: str, output_dir:str) -> None:
        headers: dict = {
            'PRIVATE-TOKEN': os.environ.get('GITLAB_PRIVATE_TOKEN')
        }
        res: response = requests.get(url, headers=headers)
        if res.status_code == 200:
            logger.info(f"Package downloaded {url}")
            destination: Path = Path(output_dir)
            if destination.is_dir():
                # check if directory exists
                shutil.rmtree(destination)
            os.mkdir(output_dir)
            z: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(res.content))
            z.extractall(path=output_dir)
        else:
            logger.exception(f"Something went wrong downloading package: {url}. Error: {res.content}")
            raise Exception(f"Error {res.status_code}")
        

    @staticmethod
    def upload_package(url: str, path_file: str) -> response:
        headers: dict = {
            'PRIVATE-TOKEN': os.environ.get('GITLAB_PRIVATE_TOKEN')
        }
        fileobj: object = open(path_file, 'rb')
        res: response = requests.put(url, headers=headers, data=fileobj.read())
        if res.status_code == 200:
            logger.info(f"Package uploaded {url}")
        else:
            logger.exception(f"Something went wrong uploading package: {url}. Error: {res.content}")
            raise Exception(f"Error {res.status_code}")

    @staticmethod
    def zip_package(output_filename: str, dir_name: str) -> None:
        try:
            shutil.make_archive(output_filename, 'zip', dir_name)
        except Exception as exc:
            logger.exception(f"Something went wrong zipping: {output_filename}. Error: {exc}")
            raise
