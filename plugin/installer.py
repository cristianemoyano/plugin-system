from urllib import response
import requests, zipfile, io

import shutil
from pathlib import Path

def install_plugin(
    zip_file_url: str,
    plugins_dir: str,
    target_plugin_name: str,
    source_plugin_path: str,
    source_root_path: str
):
    # Get file
    r: response = requests.get(zip_file_url)
    # Put in memory
    z: zipfile.ZipFile = zipfile.ZipFile(io.BytesIO(r.content))
    # Extract content
    z.extractall(
        path=plugins_dir,
    )
    # Move directory
    destination: Path = Path(f"{plugins_dir}/{target_plugin_name}")
    if destination.is_dir():
        # check if directory exists
        shutil.rmtree(destination)
    shutil.move(src=f'{plugins_dir}/{source_plugin_path}', dst=f'{plugins_dir}/')
    shutil.rmtree(Path(f"{plugins_dir}/{source_root_path}"))

if __name__ == "__main__":
    TARGETS_PLUGIN_NAMES: list[str] = [
        'printer',
        'hello',
    ]

    for target_plugin_name in TARGETS_PLUGIN_NAMES:

        PLUGINS_DIR: str = 'plugins'
        SOURCE_ROOT_PATH: str = 'plugin-system-main'
        SOURCE_PLUGIN_PATH: str = f'plugin-system-main/plugin/plugins/{target_plugin_name}/'
        ZIP_FILE_URL: str = "https://github.com/cristianemoyano/plugin-system/archive/refs/heads/main.zip"

        install_plugin(
            zip_file_url=ZIP_FILE_URL,
            plugins_dir=PLUGINS_DIR,
            target_plugin_name=target_plugin_name,
            source_plugin_path=SOURCE_PLUGIN_PATH,
            source_root_path=SOURCE_ROOT_PATH,
        )
