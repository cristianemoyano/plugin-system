"""Factory for creating a game character."""
from glob import glob
import logging
from typing import Any, Callable, Iterable, List
from collections.abc import Mapping

from plugin_manager.interface import PluginInterface, MainPlugin

logger: logging.Logger = logging.getLogger(__name__)

class AppHooks:
    INIT_APP: str = 'init'
    ACTIVATE_PLUGIN: str = 'activate_plugin_{}'
    DESACTIVATE_PLUGIN: str = 'desactivate_plugin_{}'
    UNINSTALL_PLUGIN: str = 'uninstall_plugin_{}'


plugins: dict[str, PluginInterface] = {}
actions: dict[str, List[dict[str, dict]]] = {}
activated_plugins: set = set()
is_main_plugin_activated: bool = False

def get_meta_attr(plugin_class: PluginInterface, attribute: str) -> str:
    return getattr(plugin_class.Meta, attribute)

def set_meta_attr(plugin_class: PluginInterface, attribute: str, value: Any) -> str:
    return setattr(plugin_class.Meta, attribute, value)

def setup() -> None:
    if get_meta_attr(MainPlugin, 'is_enabled') is True:
        logger.info("App already initiated.")
        return
    register(MainPlugin)
    MainPlugin.setup_callback()
    add_action(
        hook_name=AppHooks.INIT_APP,
        callback=MainPlugin.init_callback,
        args=None,
        priority=10,
        plugin=MainPlugin,
    )
    activate(get_meta_attr(MainPlugin, 'plugin_name'))
    set_meta_attr(MainPlugin, 'is_enabled', True)

def activate(plugin_name: str) -> None:
    if plugin_name in activated_plugins:
        logger.info(f"Plugin {plugin_name} already activated")
        return
    # Activate plugin
    activated_plugins.add(plugin_name)
    # Call activate plugin hook
    do_action(AppHooks.ACTIVATE_PLUGIN.format(plugin_name))

def desactivate(plugin_name: str) -> None:
    # Call desactivate plugin hook
    do_action(AppHooks.DESACTIVATE_PLUGIN.format(plugin_name))
    # Desactivate plugin
    try:
        activated_plugins.remove(plugin_name)
    except KeyError:
        logger.info(f"Plugin {plugin_name} already desactivated")


def register(plugin_class: PluginInterface) -> None:
    """Register a new game plugin type."""
    plugin_name: str = get_meta_attr(plugin_class, 'plugin_name')
    plugins[plugin_name] = plugin_class
    add_action(
        hook_name=AppHooks.ACTIVATE_PLUGIN.format(plugin_name),
        callback=plugin_class.register_activation_hook,
        args=None,
        priority=10,
        plugin=plugin_class,
    )
    add_action(
        hook_name=AppHooks.DESACTIVATE_PLUGIN.format(plugin_name),
        callback=plugin_class.register_deactivation_hook,
        args=None,
        priority=10,
        plugin=plugin_class,
    )
    add_action(
        hook_name=AppHooks.UNINSTALL_PLUGIN.format(plugin_name),
        callback=plugin_class.register_uninstall_hook,
        args=None,
        priority=10,
        plugin=plugin_class,
    )


def unregister(name: str) -> None:
    """Unregister a game plugin type."""
    plugins.pop(name, None)



def add_action(hook_name: str, plugin: PluginInterface, callback: Callable, args: list, priority: int):
    if actions.get(hook_name) is None:
        actions[hook_name] = []

    actions[hook_name].append({
        'callback': callback,
        'args': args,
        'priority': priority,
        'plugin': plugin,
    })


def do_action(hook_name: str) -> None:
    "Calls the callback functions that have been added to an action hook."
    hooks: list = actions[hook_name]
    for hook in hooks:
        plugin: PluginInterface = hook['plugin']
        if get_meta_attr(plugin, 'plugin_name') not in activated_plugins:
            continue

        callback: Callable = hook['callback']
        args: Any = hook['args']
        if isinstance(args, Mapping):
            callback(**args)
        elif isinstance(args, Iterable):
            callback(*args)
        else:
            callback()
