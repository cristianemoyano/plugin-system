import io
import os
from pathlib import Path
import shutil
import zipfile
import requests
from urllib import response


from plugin_manager import interface
from plugin_manager import loader

class PackageService:

    @staticmethod
    def list_packages(path) -> list:
        dir_list: list[str] = os.listdir(path)
        dir_list.remove('__init__.py')
        plugin_list: list = []
        for plugin_import in map(lambda directory: f'{path}.{directory}', dir_list):
            plugin_module: loader.ModuleInterface = loader.import_plugin_module(plugin_import)
            # Get the main plugin class
            plugin_class: interface.PluginInterface = plugin_module.register()
            plugin_meta: dict[str, str] = interface.get_plugin_metadata(plugin_class)
            plugin_list.append(plugin_meta)
        return plugin_list

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

