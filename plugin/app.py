"""
Basic example showing how to run custom routines from data using a dynamic factory with
activate/desactivate methods.
"""
import logging
import os

from plugin_manager import functions, loader

logger: logging.Logger = logging.getLogger(__name__)

def get_import_name(directory) -> str:
    return f'plugins.{directory}'

def get_plugins_installed() -> list[str]:
    path: str = "plugins"
    dir_list: list[str] = os.listdir(path)
    dir_list.remove('__init__.py')
    return map(get_import_name, dir_list)

def main() -> None:
    """example app"""
    # Setup main plugin
    functions.setup()

    # Perfom INIT_APP action: Should run only main plugin
    functions.do_action(functions.AppHooks.INIT_APP)

    # Print plugins found
    plugins_installed: list[str] = list(get_plugins_installed())
    logger.info(f"Plugins found: {plugins_installed}")

    # Load the plugins from directory
    loader.load_plugins(plugins_installed)

    # Activate plugins
    functions.activate('printer')
    functions.activate('hello')

    # Perfom INIT_APP action: Should run all plugin's hook
    functions.do_action(functions.AppHooks.INIT_APP)

    # Activate 'printer' plugin again. This has no effect. 
    functions.activate('printer')

    # Desactivate 'hello' plugin
    functions.desactivate('hello')
    # Desactivate 'hello' plugin again. This has no effect.
    functions.desactivate('hello')

    # Perfom INIT_APP action: Should run only printer plugin's hook since still activated
    functions.do_action(functions.AppHooks.INIT_APP)

if __name__ == "__main__":
    main()
