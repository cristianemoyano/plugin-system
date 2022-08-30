"""A simple plugin loader."""
import importlib
from typing import Any

from plugin_manager.interface import PluginInterface
from plugin_manager import functions

class ModuleInterface:
    """Represents a plugin interface"""

    @staticmethod
    def register() -> None:
        """Register the plugin"""

    @staticmethod
    def add_actions() -> list[dict[str, Any]]:
        """Add actions"""


def import_module(name: str) -> ModuleInterface:
    """Imports a module given a name."""
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    """Loads the plugins defined in the plugins list."""
    for plugin_file in plugins:
        # Import plugin
        plugin_module: ModuleInterface = import_module(plugin_file)
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
