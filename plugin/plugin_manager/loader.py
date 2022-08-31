"""A simple plugin loader."""
import importlib
from typing import Any

from plugin_manager.interface import PluginInterface
from plugin_manager import functions

class ModuleInterface:
    """Represents a plugin interface"""

    # Optional: Set this attribute in the __init__.py file of your root plugin directory to specify the main plugin file name
    # in case that this file name is different from the root plugin directory name: my_plugin_folder/main.py
    # example for a main.py:
    # 
    # PLUGIN_MODULE = 'main'
    # 
    # The default value is the root plugin directory name: PLUGIN_MODULE = '<plugin directory name>'
    PLUGIN_MODULE_KEYWORD: str = 'PLUGIN_MODULE'

    @staticmethod
    def register() -> None:
        """Register the plugin"""

    @staticmethod
    def add_actions() -> list[dict[str, Any]]:
        """Add actions"""


def import_module(name: str) -> ModuleInterface:
    """Imports a module given a name."""
    return importlib.import_module(name)  # type: ignore

def import_plugin_module(plugin_module: str) -> ModuleInterface:
    plugin_root_module: ModuleInterface = import_module(plugin_module)
    plugin_main_file_name: str= getattr(plugin_root_module, ModuleInterface.PLUGIN_MODULE_KEYWORD, plugin_module.split('.')[-1])
    plugin_module: ModuleInterface = import_module(f'{plugin_module}.{plugin_main_file_name}')
    return plugin_module


def load_plugins(plugins: list[str]) -> None:
    """Loads the plugins defined in the plugins list."""
    for plugin_file in plugins:
        # Import plugin
        plugin_module: ModuleInterface = import_plugin_module(plugin_file)
        # Get the main plugin class
        plugin_class: PluginInterface = plugin_module.register()
        # Register the plugin
        functions.register(plugin_class)
        # Add all the actions
        for action in plugin_module.add_actions():
            functions.add_action(
                hook_name=action['hook_name'],
                callback=action['callback'],
                args=action.get('args'),
                plugin=plugin_class,
                priority=action.get('priority', 10),
            )
