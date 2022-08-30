from urllib import response
import requests, zipfile, io

import shutil
from pathlib import Path

PLUGINS_DIR: str = 'plugins'
TARGET_PLUGIN_NAME: str = 'printer'
SOURCE_ROOT_PATH: str = 'plugin-system-main'
SOURCE_PLUGIN_PATH: str = f'plugin-system-main/plugin/plugins/{TARGET_PLUGIN_NAME}/'
ZIP_FILE_URL: str = "https://github.com/cristianemoyano/plugin-system/archive/refs/heads/main.zip"

def install_plugin(zip_file_url: str):
    # Get file
    r: response = requests.get(zip_file_url)
    # Put in memory
    z: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(r.content))
    # Extract content
    z.extractall(
        path=PLUGINS_DIR,
    )
    # Move directory
    destination: Path = Path(f"{PLUGINS_DIR}/{TARGET_PLUGIN_NAME}")
    if destination.is_dir():
        # check if directory exists
        shutil.rmtree(destination)
    shutil.move(src=f'{PLUGINS_DIR}/{SOURCE_PLUGIN_PATH}', dst=f'{PLUGINS_DIR}/')
    shutil.rmtree(Path(f"{PLUGINS_DIR}/{SOURCE_ROOT_PATH}"))

if __name__ == "__main__":
    install_plugin(ZIP_FILE_URL)
