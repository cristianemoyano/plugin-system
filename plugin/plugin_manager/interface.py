from typing import Protocol
import logging

logger: logging.Logger = logging.getLogger(__name__)


class PluginInterface(Protocol):
    """Basic representation of a plugin."""

    class Meta:
        # Required
        plugin_name: str = 'The name of your plugin'
        # Optional
        plugin_uri: str = 'The home page of the plugin, which should be a unique URL, preferably on your own website.'
        plugin_description: str = 'A short description of the plugin'
        version: str = 'The current version number of the plugin, such as 1.0 or 1.0.3'
        author: str = 'The name of the plugin author. Multiple authors may be listed using commas.'
        license: str = 'The short name (slug) of the plugin’s license (e.g. GPLv2)'

    @staticmethod
    def register_activation_hook() -> None:
        """
        On activation, plugins can run a custom routine.
        """
        pass

    @staticmethod
    def register_deactivation_hook() -> None:
        """
        On deactivation, plugins can run a routine to remove temporary data such as cache and temp files and directories.
        """
        pass

    @staticmethod
    def register_uninstall_hook() -> None:
        pass



class MainPlugin(PluginInterface):

    class Meta:
        plugin_name: str = '__mainplugin__'
        is_enabled: bool = False
    
    @staticmethod
    def setup_callback() -> None:
        if MainPlugin.Meta.is_enabled is True:
            logger.info("App already initiated.")
        FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt='%d-%b-%y %H:%M:%S')
        logger.debug("App initiated")
    
    @staticmethod
    def init_callback() -> None:
        logger.debug("Init called")

    @staticmethod
    def register_activation_hook() -> None:
        logger.debug(f"register_activation_hook: {MainPlugin.Meta.plugin_name}")

    @staticmethod
    def register_deactivation_hook() -> None:
        logger.debug(f"register_deactivation_hook: {MainPlugin.Meta.plugin_name}")

    @staticmethod
    def register_uninstall_hook() -> None:
        logger.debug(f"register_uninstall_hook: {MainPlugin.Meta.plugin_name}")


def get_plugin_metadata(plugin_class: PluginInterface) -> dict[str, str]:
    return {
        'name': plugin_class.Meta.plugin_name,
        'plugin_uri': plugin_class.Meta.plugin_uri,
        'plugin_description': plugin_class.Meta.plugin_description,
        'version': plugin_class.Meta.version,
        'author': plugin_class.Meta.author,
        'license': plugin_class.Meta.license,
    }
